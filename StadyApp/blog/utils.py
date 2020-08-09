from django.shortcuts import render, get_object_or_404


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        # tag = Tag.objects.get(slug__iexact=slug)
        # возврашаем объект или ошибку 404
        object = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): object})


