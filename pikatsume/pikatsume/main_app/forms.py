from django import forms
from .models import Pika, Profile

class PikaForm(forms.ModelForm):
    class Meta:
        model = Pika
        fields = ('name', 'pic')


