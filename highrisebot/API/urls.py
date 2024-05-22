from django.urls import path
from .views import BotModeratorGet, HighrisePlayersAPI

urlpatterns = [
    path('api/bots/', BotModeratorGet.as_view(), name='bots'),
    path('api/players/', HighrisePlayersAPI.as_view(), name='players'),
]
