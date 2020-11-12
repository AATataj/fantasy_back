from django.urls import re_path, path


from . import consumers

websocket_urlpatterns = [
    ## I don't think I need a landing spot for scrapeAll as the sockets will 
    ## be requested individually from front end
    # path('ScrapeAll/', consumers.ProgressAll.as_asgi()),
    path('ScrapeRoto/', consumers.ProgressRoto.as_asgi()),
    path('ScrapeBox/', consumers.ProgressBox.as_asgi()),
    path('ScrapePlays/', consumers.ProgressPlay.as_asgi()),
]