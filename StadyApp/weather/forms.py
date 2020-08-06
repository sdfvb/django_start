from django.core.exceptions import ValidationError

from .models import City
from django.forms import ModelForm, TextInput


class CityForm(ModelForm):
    """ Формы джанго """

    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'form-control',
                                            'name': 'city',
                                            'id': 'city',
                                            'placeholder': 'Введите город'
                                            })}

    def clean_name(self):
        new_name = self.cleaned_data['name']

        if City.objects.filter(name=new_name).count():
            raise ValidationError(f'Город {new_name} уже в списке')

        return new_name
