from .actions import ActionResult
from .message_parser import MessageParser
from .data_store import DataStore
from .response import ResponseBuilder


class MessageHandler():

    def __init__(self, message_parser: MessageParser, data_store: DataStore, response_builder: ResponseBuilder):
        self.message_parser = message_parser
        self.data_store = data_store
        self.response_builder = response_builder

    def handle_message(self, message: str) -> str:
        response = None

        try:
            action = self.message_parser.parse_json(message)

            result = self.data_store.run_action(action)

            response = self.response_builder.build_response_from_result(result)

        except Exception as exception:
            response = self.response_builder.build_response_from_error(exception)

        return response
