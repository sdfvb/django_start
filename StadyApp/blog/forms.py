from django import forms
from django.core.exceptions import ValidationError

from .models import Tag, Post


# class TagForm(forms.Form):
#     # генерирует html формы
#     title = forms.CharField(max_length=150)
#     slug = forms.SlugField(max_length=150)
#
#     title.widget.attrs.update({'class': 'form-control'})
#     slug.widget.attrs.update({'class': 'form-control'})

# def save(self):
#     new_tag = Tag.objects.create(
#         title=self.cleaned_data['title'],
#         slug=self.cleaned_data['slug']
#     )
#     return new_tag

class TagForm(forms.ModelForm):
    # генерирует html формы
    # данный класс уже связан с моделью

    class Meta:
        model = Tag
        fields = ['title', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        # спец метод для проверки поля slug
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug не может быть create')

        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Slug должен быть уникальный, slug-{new_slug} уже существует')

        return new_slug

    # def save(self):
    #     new_tag = Tag.objects.create(
    #         title=self.cleaned_data['title'],
    #         slug=self.cleaned_data['slug']
    #     )
    #     return new_tag


class PostForm(forms.ModelForm):
    # генерирует html формы
    # данный класс уже связан с моделью

    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        # спец метод для проверки поля slug
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug не может быть create')

        # if Tag.objects.filter(slug__iexact=new_slug).count():
        #     raise ValidationError(f'Slug должен быть уникальный, slug-{new_slug} уже существует')

        return new_slug

    # def save(self):
    # не нужен при ModelForm
    #     new_tag = Post.objects.create(
    #         title=self.cleaned_data['title'],
    #         slug=self.cleaned_data['slug'],
    #         body=self.cleaned_data['body'],
    #         tags=self.cleaned_data['tags']
    #     )
    #     return new_tag
