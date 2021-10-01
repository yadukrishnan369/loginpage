from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.test2fun,name='test2'),
    path('login',views.loginfun,name='login'),
]