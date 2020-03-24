from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('about/', views.about, name='about'),
    path('pikabase/', views.pikabase_index, name='index'),
    path('pikabase/new/', views.new_pika, name='new_pika'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_form'),    
    path('accounts/signup', views.signup, name='signup'),
    path('catch/', views.catch, name='catch'),
    path('catch/confirm', views.catch_confirm, name='catch_confirm'),
    path('caught/', views.caught, name='caught'),
    path('profile/delete', views.delete_profile, name='delete_profile'),
    path('store/', views.store, name='store'),
    path('store/success', views.success, name='success'),
    path('store/cancel', views.cancel, name='cancel'),
]