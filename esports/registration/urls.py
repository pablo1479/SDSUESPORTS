from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('home/', views.index, name='home'),  # Empty path for the root of the site
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('application/', views.application, name='application'),
    path('stats/', views.stats, name='stats'),
    path('contact/', views.contact, name='contact'),
    path('merch/', views.merch, name='merch'),
    path('stream/', views.stream, name='stream'),
]

