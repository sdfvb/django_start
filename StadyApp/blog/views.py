from django.shortcuts import render
from django.views.generic.base import View

from .forms import TagForm
from .models import Post, Tag
from .utils import ObjectDetailMixin


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(View):

    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})
