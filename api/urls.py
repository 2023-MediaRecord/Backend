from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
  path("login", views.login, name='login'),
  path('users/', views.UserList.as_view(), name='user-list'),
  path('records', views.record_list, name='record-list')
]