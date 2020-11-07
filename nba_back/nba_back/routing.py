from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'/ScrapeAll/', consumers.ProgressConsumer.as_asgi()),
    re_path(r'/ScrapeRoto/', consumers.ProgressConsumer.as_asgi()),
    re_path(r'/ScrapeBox/', consumers.ProgressConsumer.as_asgi()),
    re_path(r'/ScrapePlays/', consumers.ProgressConsumer.as_asgi()),
]