from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from .models import PostCKEditor


class PostView(ListView):
    template_name = "CkedTemp/blog.html"
    model = PostCKEditor

#
# class PostView(DetailView):
#     model = PostCKEditor
#     template_name = "CkedTemp/blog.html"