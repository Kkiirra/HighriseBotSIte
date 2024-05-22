from django.shortcuts import render
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'main/dashboard.html'


class BotsPageView(TemplateView):
    template_name = 'main/botspage.html'
