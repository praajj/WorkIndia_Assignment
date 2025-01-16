from django.contrib import admin
from django.urls import path
from IRCTC_App import views

urlpatterns = [
    path("", views.index, name='home'),
]
