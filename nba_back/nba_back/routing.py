from django.urls import re_path, path


from . import consumers

websocket_urlpatterns = [
    path('ScrapeAll/', consumers.ProgressConsumer.as_asgi()),
    path('ScrapeRoto/', consumers.ProgressConsumer.as_asgi()),
    path('ScrapeBox/', consumers.ProgressConsumer.as_asgi()),
    path('ScrapePlays/', consumers.ProgressConsumer.as_asgi()),
]