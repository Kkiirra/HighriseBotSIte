from django.urls import path
from .views import DashboardView, BotsPageView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('bots/', BotsPageView.as_view(), name='bots'),
]
