from django.urls import path
from . import views
from .views import LoginView
from .views import ProfileView
from .views import profile_view
from .views import logout_view

urlpatterns = [
    path('home/', views.index, name='home'),  # Empty path for the root of the site
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('application/', views.application, name='application'),
    path('stats/', views.stats, name='stats'),
    path('contact/', views.contact, name='contact'),
    path('merch/', views.merch, name='merch'),
    path('stream/', views.stream, name='stream'),
    path('api/login/', LoginView.as_view(), name='api_login'),
    path('api/profile/', ProfileView.as_view(), name='profile'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('submit_application/', views.submit_application, name='submit_application'),


]

