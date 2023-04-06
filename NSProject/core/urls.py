from django.urls import path

from .views import HomeView, Login, Register



urlpatterns = [ 
    path('', HomeView.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    
    ]