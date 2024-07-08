"""
ASGI config for Unnotech_HW project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.security.websocket import OriginValidator
from nba_news.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Unnotech_HW.settings")

django_asgi_app = get_asgi_application()
application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        # Just HTTP for now. (We can add other protocols later.)
        "websocket": OriginValidator(
            (URLRouter(websocket_urlpatterns)), allowed_origins=["*"]
        ),
    }
)
