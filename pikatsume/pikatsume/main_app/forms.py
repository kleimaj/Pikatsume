from django import forms
from .models import Pika, Profile

class PikaForm(forms.ModelForm):
    class Meta:
        model = Pika
        fields = ('name', 'pic_url')

from django.contrib.auth.models import User

class Profile(forms.ModelForm):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
