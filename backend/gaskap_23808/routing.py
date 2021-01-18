import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from chat.token_auth import TokenAuthMiddleware
import chat.routing


application = ProtocolTypeRouter(
    {
        "websocket": TokenAuthMiddleware(
            AuthMiddlewareStack(URLRouter(chat.routing.websocket_urlpatterns)),
        ),
    }
)
