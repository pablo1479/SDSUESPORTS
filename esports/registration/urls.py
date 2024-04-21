from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('', views.home, name='home'),  # Empty path for the root of the site
]