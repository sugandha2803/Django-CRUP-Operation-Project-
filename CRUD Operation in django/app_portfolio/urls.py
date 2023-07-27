from django.contrib import admin
from django.urls import path
from app_portfolio import views

urlpatterns = [
    path('', views.index, name="index"),
   
]
