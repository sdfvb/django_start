from django import forms
from django.core.exceptions import ValidationError

from .models import Tag


class TagForm(forms.Form):
    # генерирует html формы
    title = forms.CharField(max_length=150)
    slug = forms.SlugField(max_length=150)

    def clean_slug(self):
        # спец метод для проверки поля slug
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug не может быть create')
        return new_slug

    def save(self):
        new_tag = Tag.objects.create(
            title=self.cleaned_data['title'],
            slug=self.cleaned_data['slug']
        )
        return new_tag
