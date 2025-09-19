from django.contrib import admin
from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('note/<int:note_id>/', views.note_detail, name='detail'),
    path("users/<int:user_id>/", views.user_detail, name="user_detail"),
]
