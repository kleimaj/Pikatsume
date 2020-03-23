from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.dispatch import receiver
from .models import Pika, Profile
from .forms import PikaForm
# Create your views here.

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # profile = Profile()
            login(request, user)
            # Create default profile
            return redirect('profile')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = { 'form' : form, 'error_message' : error_message }
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return  render(request, 'about.html')

def pikabase_index(request):
    pikas = Pika.objects.all()
    return  render(request, 'pikabase/index.html', { 'pikas': pikas })

@login_required
def profile(request):
    # profile = Profile(name=request.user, poffins=30)
    # print(profile)
    # profile.save()
    # print("profile saved~~~~~~~")
    return render(request, 'accounts/profile.html')

@login_required
def new_pika(request):
    if request.method == 'POST':
        new_form = PikaForm(request.POST)
        if new_form.is_valid():
            pika = new_form.save(commit="False")
            pika.user = request.user
            pika.save()
            return redirect ('pikabase/index.html', pika.id)
    else:
        new_form = PikaForm()
        context = {  'new_form' : new_form  }
        return render(request, 'pikabase/pika_form.html', context)

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile.html')
    else:
        profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'profile.html', {'profile_form': profile_form})

def delete_profile(request, car_id):
    Profile.objects.get(id=profile_id).delete()
    return redirect('index') 
     
# Catch (Game Logic Controllers)
@login_required
def catch(request):
    return render(request, 'catch/catch.html')
@login_required
def catch_confirm(request):
    # user = request.user
    # print(user)
    # profile = user.profile
    profile = Profile.objects.get(user=request.user)
    profile.poffins = int(profile.poffins)
    return render(request, 'catch/catch_confirm.html', {'profile':profile})
@login_required
def caught(request):
    # get this user's profile
    profile = Profile.objects.get(user=request.user)
    print(profile.poffins)
    print(profile.pikachu)
    # decrement poffins by 5
    # profile.poffins -= 5
    new_pika = Pika.objects.order_by("?").first()
    profile.pikachu.add(new_pika.id)
    return render(request, 'catch/caught.html', {
        'pika':new_pika,
        'profile':profile,
        })