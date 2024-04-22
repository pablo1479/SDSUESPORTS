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
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.exceptions import ValidationError  # Importing ValidationError

# Function to handle user registration via form
def register_form(request):
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
    return redirect(reverse('home'))

# API view to handle user registration via API
@csrf_exempt
def register_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user = User.objects.create_user(
                username=data['email'],
                email=data['email'],
                password=data['password'],
                first_name=data['first_name'],
                last_name=data['last_name']
            )
            user.full_clean()
            user.save()
            return JsonResponse({'success': True, 'message': 'User registered successfully'}, status=201)
        except ValidationError as ve:
            return JsonResponse({'success': False, 'message': str(ve.messages)}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'Failed to register user'}, status=400)
    return JsonResponse({'success': False, 'message': 'Only POST method is allowed'}, status=405)
