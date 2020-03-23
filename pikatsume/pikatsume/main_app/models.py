from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
ORIGIN = (
    ('A', 'Anime'),
    ('G', 'Game'),
    ('F', 'Fan-made'),
)
class Ptype(models.Model):
    pika_type = models.CharField(max_length=100)
    
    def __str__(self):
        return self.pika_type

class Pika(models.Model):
    name = models.CharField(max_length=255)
    pic = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=255)
    poffins = models.CharField(max_length=500)
    pikachu = models.ManyToManyField(Ptype)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()