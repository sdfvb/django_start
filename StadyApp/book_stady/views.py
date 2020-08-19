from django.shortcuts import render
from django.views.generic import TemplateView


class BookPageView(TemplateView):
    template_name = 'home_page.html'
