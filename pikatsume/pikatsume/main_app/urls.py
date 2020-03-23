from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
    
    path('about/', views.about, name='about'),
    
    path('pikabase/', views.pikabase_index, name='index'),
    path('pikabase/new/', views.new_pika, name='new_pika'),
    
    path('profile/', views.profile, name='profile'),
<<<<<<< HEAD
    path('accounts/signup', views.signup, name='signup'),
=======
    path('profile/edit/', views.profile_edit, name='profile_form'), 

>>>>>>> 2ae9fa8fcf2a4644c1b45a38634f0de0fce2e06d
    path('catch/', views.catch, name='catch'),
    path('catch/confirm', views.catch_confirm, name='catch_confirm'),
    path('caught/', views.caught, name='caught'),
    path('profile/', views.profile_detail, name='profile_detail'),
    path('profile/<int:profile_id>/delete', views.delete_profile, name='delete_profile'),
    path('profile/<int:profile_id>/edit', views.update_profile, name='update_profile')

]