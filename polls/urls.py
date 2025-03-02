
from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.gra, name='muzyka'),  
    path('login/', views.user_login, name='login'),
    path('gra/', views.gra, name='muzyka'),
    path('logout/', views.logout_view, name='logout'),   
    path('rejestr/', views.register, name='rejestr'),
    path('button_click/<str:action>/', views.button_click, name='button_click'),

]
