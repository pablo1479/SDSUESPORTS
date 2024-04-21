"""
URL configuration for your ESports website.

The `urlpatterns` list routes URLs to views. For more information, please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from .. import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("registration/", views.registration, name="registration"),
    path("application/", views.application, name="application"),
    path("stats/", views.statistics, name="statistics"),
    path("contact/", views.contact, name="contact"),
    path("admin/", admin.site.urls),
]
