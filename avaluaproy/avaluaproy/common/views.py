from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'common/home.html'


class PanelView(TemplateView):
    template_name = 'common/panel.html'