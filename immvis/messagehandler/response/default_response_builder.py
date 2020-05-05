from .response_builder import ResponseBuilder
from ..actions.action_result import ActionResult
from pandas import DataFrame
import numpy as np
from .json_encoder import ImmVisJsonEncoder
import json

_FIELD_TYPE = 'object_type'
_FIELD_CAUSE = 'cause'
_FIELD_MESSAGE = 'message'
_TYPE_ERROR = 'error'
_FIELD_TYPE = 'object_type'
_FIELD_COLUMNS = 'columns'
_FIELD_COLUMNS_TYPES = 'columns_types'
_FIELD_VALUES = 'values'
_FIELD_DATA = 'data'
_FIELD_AXIS_LABELS = 'axis_labels'


class DefaultResponseBuilder(ResponseBuilder):
    def build_response_from_result(self, action_result: ActionResult) -> str:
        response = {
            _FIELD_TYPE: action_result.type_name,
            _FIELD_DATA: self._build_data_field(action_result.data)
        }

        return self._convert_object_to_json_str(response)

    def build_response_from_error(self, error: Exception) -> str:
        error_obj = {
            _FIELD_TYPE: _TYPE_ERROR,
            _FIELD_CAUSE: error.__class__.__name__
        }

        message = error.args[0]

        if message is not None:
            error_obj[_FIELD_MESSAGE] = str(message)

        return self._convert_object_to_json_str(error_obj)

    def _build_data_field(self, data: object) -> object:
        data_obj = {}

        if type(data) is DataFrame:
            data_fields = self._build_data_fields_from_data_frame(data)

            for key, value in data_fields.items():
                if type(key) is str and value is not None:
                    data_obj[key] = value
        else:
            data_obj = data

        return data_obj

    def _build_data_fields_from_data_frame(self, data_frame: DataFrame) -> dict:
        data_obj = {}

        data_obj[_FIELD_VALUES] = self._normalize_values(data_frame).values

        data_obj[_FIELD_COLUMNS] = list(map(
            lambda column: str(column), data_frame.columns))

        data_obj[_FIELD_COLUMNS_TYPES] = list(map(
            lambda type: str(type), data_frame.dtypes))

        return data_obj

    def _normalize_values(self, data_frame: DataFrame) -> DataFrame:
        result = data_frame.copy()

        for column_name in result.columns:
            column = result[column_name]

            if not np.issubdtype(column.dtype, np.number):
                column = column.factorize()[0]

            max_value = column.max()

            min_value = column.min()

            result[column_name] = (column - min_value) / \
                (max_value - min_value)

        return result

    def _convert_object_to_json_str(self, message_object: object):
        return json.dumps(message_object, cls=ImmVisJsonEncoder)
