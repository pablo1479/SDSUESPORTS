from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework import status, views
from rest_framework.permissions import IsAuthenticated


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/success.html')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# Generic views for other pages
def index(request):
    return render(request, 'registration/index.html')

def about(request):
    return render(request, 'registration/about.html')

def application(request):
    return render(request, 'registration/application.html')

def stats(request):
    return render(request, 'registration/stats.html')

def contact(request):
    return render(request, 'registration/contacts.html')

def merch(request):
    return render(request, 'registration/merch.html')

def stream(request):
    return render(request, 'registration/stream.html')

# API view to handle user login
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# API view to provide user profile information
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_data = {
            "username": request.user.username,
            "email": request.user.email
        }
        return Response(user_data)



























# View for user profile page
def profile_view(request):
    return render(request, 'registration/profile.html')

# Function to handle user logout
def logout_view(request):
    logout(request)
    return redirect('/home')  # Redirect to home page after logout