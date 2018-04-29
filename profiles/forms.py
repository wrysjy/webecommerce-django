from django.forms import ModelForm

from .models import product


class ManageForm(ModelForm):
    class Meta:
        model = product
        fields = ['name', 'description', 'image', 'category']
