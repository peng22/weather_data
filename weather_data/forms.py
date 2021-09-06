from .models import *
from django.forms import ModelForm


class Weather_Data_form(ModelForm):
     class Meta:
         model = Weather_Data
         fields = ['temperature', 'humidity']
