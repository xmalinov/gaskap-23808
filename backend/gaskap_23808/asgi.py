import os

import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from chat.token_auth import TokenAuthMiddleware
import chat.routing


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gaskap_23808.settings")
django.setup()

application = ProtocolTypeRouter(
    {
        "http": AsgiHandler(),
        "websocket": TokenAuthMiddleware(
            AuthMiddlewareStack(URLRouter(chat.routing.websocket_urlpatterns)),
        ),
    }
)
