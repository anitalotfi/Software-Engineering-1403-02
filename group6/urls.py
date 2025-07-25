from django.urls import path
from . import views

app_name = 'group6'

urlpatterns = [
  path('', views.home, name='group6'),
  path('start_session/', views.start_learning_session, name='start_learning_session'),
  path('process_guess/', views.process_guess, name='process_guess'), # process user's guess or navigate session
  path('signup/', views.group6_signup, name='signup'), 
  path('login/', views.group6_login, name='login'),
  path('logout/', views.group6_logout, name='logout'), 
] 