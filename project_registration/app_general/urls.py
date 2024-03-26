from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name = 'home'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
]