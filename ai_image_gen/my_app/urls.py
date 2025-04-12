

from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.prompt_input, name='prompt_input'),
    path('generate/', views.generate_image, name='generate_image'),
]