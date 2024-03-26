from django.urls import path ,include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', views.register ,name = 'register'),
    path('register/thankyou', views.register_thankyou ,name = 'register_thankyou'),
    path('profile', views.profile ,name = 'profile'),
]