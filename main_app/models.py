from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os, time
import datetime

class Pika(models.Model):
    name = models.CharField(max_length=255)
    pic = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

class Profile(models.Model):        
    name = models.CharField(max_length=255)
    # loginTime = models.CharField(max_length=255)
    loginTime = models.DateTimeField()
        
    poffins = models.IntegerField()
    
    pikachu = models.ManyToManyField(Pika)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print("~~~~~~~~~")
        # print(instance)
        # print(instance.user)
        # print(instance.username)
        # userLoginTime = time.strftime('%X %x %Z')
        # print(userLoginTime)
        userLoginTime = datetime.datetime.now()
        
        Profile.objects.create(user=instance, loginTime=userLoginTime, poffins=30, name=instance.username)
    
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    print("HERE!")