"""
ASGI config for dermit project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from chat.middleware import TokenAuthMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dermit.settings')

django_asgi_application = get_asgi_application()

from chat.routing import websocket_urlpatterns

application = ProtocolTypeRouter(
    {
        "http": django_asgi_application,
        # "websocket": AllowedHostsOriginValidator(
        #     TokenAuthMiddleware(URLRouter(websocket_urlpatterns))
        # ),
        "websocket": TokenAuthMiddleware(URLRouter(websocket_urlpatterns)),
    }
)
