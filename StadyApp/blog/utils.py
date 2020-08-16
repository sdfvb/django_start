from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse


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


class ObjectUpdateMixin():
    model = None
    form_model = None
    template = None

    def get(self, request, slug):
        object = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form_model(instance=object)
        return render(request, self.template, context={
            'form': bound_form,
            self.model.__name__.lower(): object,
        })

    def post(self, request, slug):
        object = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form_model(request.POST, instance=object)

        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        return render(request, self.template, context={
            'form': bound_form,
            self.model.__name__.lower(): object,
        })


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        object = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): object})

    def post(self, request, slug):
        object = self.model.objects.get(slug__iexact=slug)
        object.delete()
        return redirect(reverse(self.redirect_url))
