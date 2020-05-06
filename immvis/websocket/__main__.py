import tornado.ioloop
import tornado.web
import tornado.websocket
from .websocket_server import ImmVisWebSocket
from ..messagehandler import MessageParser, DataStore, MessageHandler
from ..messagehandler.response import ResponseBuilder, DefaultResponseBuilder
from ..discovery import DiscoveryService
import sys
import signal

_discovery_service = DiscoveryService(debug=True)
_message_parser = MessageParser()
_data_store = DataStore()
_response_builder = DefaultResponseBuilder()
_message_handler = MessageHandler(_message_parser, _data_store, _response_builder)

class ImmvisApplication(tornado.web.Application):
    should_close = False

    def signal_handler_callback(self, signum, frame):
        self.should_close = True
        print("Requested to stop the server!")

    def try_exit(self):
        if self.should_close:
            print("Stopping the server...")
            _discovery_service.stop()
            tornado.ioloop.IOLoop.instance().stop()
            print("Server stopped!")


def create_app() -> tornado.web.Application:
    _discovery_service.start()

    return ImmvisApplication([
        (
            r"/websocket",
            ImmVisWebSocket,
            {
                'message_handler': _message_handler,
                'discovery_service': _discovery_service
            }
        )
    ])


if sys.platform.startswith('win') and sys.version_info > (3, 8):
    import asyncio
    try:
        from asyncio import WindowsSelectorEventLoopPolicy
    except ImportError:
        pass
    else:
        if not isinstance(asyncio.get_event_loop_policy(), WindowsSelectorEventLoopPolicy):
            asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

if __name__ == "__main__":
    _PORT = 8888

    application = create_app()

    signal.signal(signal.SIGINT, application.signal_handler_callback)
    server = tornado.httpserver.HTTPServer(application)
    server.listen(str(_PORT))

    print("Starting server: http://localhost:" + str(_PORT) + "/")

    tornado.ioloop.PeriodicCallback(application.try_exit, 100).start()
    tornado.ioloop.IOLoop.instance().start()
