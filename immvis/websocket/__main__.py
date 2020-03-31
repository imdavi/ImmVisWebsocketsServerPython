import tornado.ioloop
import tornado.web
import tornado.websocket
from .websocket_server import ImmVisWebSocket
from ..messagehandler import MessageParser, DataStore, MessageHandler
from ..discovery import DiscoveryService
import sys

MAX_WAIT_SECONDS_BEFORE_SHUTDOWN = 3

def create_app() -> tornado.web.Application:
    message_parser = MessageParser()
    data_store = DataStore()
    message_handler = MessageHandler(message_parser, data_store)

    discovery_service = DiscoveryService(debug=True)
    discovery_service.start()

    return tornado.web.Application([
        (
            r"/websocket",
            ImmVisWebSocket,
            {
                'message_handler': message_handler,
                'discovery_service': discovery_service
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
    server = tornado.httpserver.HTTPServer(application)
    server.listen(str(_PORT))

    print("Starting server: http://localhost:" + str(_PORT) + "/")

    tornado.ioloop.IOLoop.current().start()
