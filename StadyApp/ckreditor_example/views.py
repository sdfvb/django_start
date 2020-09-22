from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from .models import PostCKEditor


class PostView(ListView):
    template_name = "CkedTemp/blog.html"
    context_object_name = 'posts'
    model = PostCKEditor
    paginate_by = 2  # and that's it !!


class PostDetail(DetailView):
    model = PostCKEditor
    template_name = "CkedTemp/blog_detail.html"
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
