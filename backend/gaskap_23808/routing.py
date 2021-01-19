import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from chat.token_auth import TokenAuthMiddleware
from chat import routing


application = ProtocolTypeRouter(
    {
        "websocket": TokenAuthMiddleware(
            AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns)),
        ),
    }
)
