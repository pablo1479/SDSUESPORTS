from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('application/', views.application, name='application'),
    path('stats/', views.stats, name='stats'),
    path('contact/', views.contact, name='contact'),
    path('merch/', views.merch, name='merch'),
    path('stream/', views.stream, name='stream'),
]
