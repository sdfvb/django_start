from django import forms


class TagForm(forms.Form):
    # генерирует html формы
    title = forms.CharField(max_length=150)
    slug = forms.SlugField(max_length=150)