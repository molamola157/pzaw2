
from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.gra, name='muzyka'),  
    path('login/', views.user_login, name='login'),
    path('login/', auth_views.LogoutView.as_view(), name='logout'),  
    path('gra/', views.gra, name='muzyka'),
    path('rejestr/', views.register, name='register'),
    path('button_click/<str:action>/', views.button_click, name='button_click')
    
]
