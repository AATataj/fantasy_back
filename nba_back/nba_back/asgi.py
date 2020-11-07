"""
ASGI config for nba_back project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

##### not original
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import nba_back.routing
#### /not original

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nba_back.settings')

# application = get_asgi_application()

##### not original 
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            nba_back.routing.websocket_urlpatterns
        )
    ),
})
#### /not original