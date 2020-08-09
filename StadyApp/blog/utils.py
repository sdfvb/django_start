from django.shortcuts import render, get_object_or_404, redirect


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        # tag = Tag.objects.get(slug__iexact=slug)
        # возврашаем объект или ошибку 404
        object = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): object})


class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form_model(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        else:
            return render(request, self.template, context={'form': bound_form})
