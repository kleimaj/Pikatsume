from django import forms
from .models import Pika, Profile

class PikaForm(forms.ModelForm):
    class Meta:
        model = Pika
        fields = ('name', 'pic_url')

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
        # fields = ('user_id','id')