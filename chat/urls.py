from django.urls import path
from . import views

urlpatterns = [
    path('chatroom', views.chat, name='chatroom'),
    path('send_message/', views.send_message, name='send_message'),
]