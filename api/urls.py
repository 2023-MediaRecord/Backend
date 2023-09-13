from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
  path("login", views.login, name='login'),
  path('users/', views.UserList.as_view(), name='user-list'),
  path('records', views.record_list, name='record-list'),
  path('records/<int:record_id>', views.record, name='record'),
  path('mypage', views.mypage, name='mypage'),
  path('wish-medias', views.wish_medias, name='wish-media-list'),
  path('liked-medias', views.liked_medias, name='liked-media-list')
]