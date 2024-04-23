from django.urls import path
from . import views

urlpatterns = [
 path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register_form, name='register_form'),
    path('application/', views.application, name='application'),
    path('stats/', views.stats, name='stats'),
    path('contact/', views.contact, name='contact'),
    path('merch/', views.merch, name='merch'),
    path('stream/', views.stream, name='stream'),
    path('api/login/', views.LoginView.as_view(), name='api_login'),
    path('api/profile/', views.ProfileView.as_view(), name='api_profile'),
    path('profile/', views.profile_view, name='profile_page'),  # Ensure this is correct
    path('logout/', views.logout_view, name='logout'),
    path('api/register/', views.register_api, name='api_register'),
    path('submit_application/', views.submit_application, name='submit_application'),



]
