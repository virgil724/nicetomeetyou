from django.urls import re_path
from nba_news.consumer import NewsConsumer

websocket_urlpatterns = [
    re_path(r"^ws/nba/$", NewsConsumer.as_asgi()),
]
