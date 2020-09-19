from django.forms import ModelForm

from .models import PostCKEditor


class PostForm(ModelForm):
    class Meta:
        model = PostCKEditor
        fields = ['description']
