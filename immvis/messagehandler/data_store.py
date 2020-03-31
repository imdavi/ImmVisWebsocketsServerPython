from .actions import Action, TransformAction
from .actions import ActionResult
from pandas import DataFrame
from abc import ABC


class DataStore():
    data_frame: DataFrame = None

    def run_action(self, action: Action) -> ActionResult:
        result = action.process(self.data_frame)

        if result is not None:
            if isinstance(action, TransformAction):
                if isinstance(result.data, DataFrame):
                    self.data_frame = result.data
                else:
                    raise Exception(
                        'Results from transform must be a data_frame.')

        return result
