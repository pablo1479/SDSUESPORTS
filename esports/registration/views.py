from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
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

def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/success.html')
    else:
        form = RegistrationForm()
    return render(request, 'registration/index.html')

def about(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/success.html')
    else:
        form = RegistrationForm()
    return render(request, 'registration/about.html')

def application(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/success.html')
    else:
        form = RegistrationForm()
    return render(request, 'registration/Application.html')

def stats(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/success.html')
    else:
        form = RegistrationForm()
    return render(request, 'registration/stats.html')

def contact(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/success.html')
    else:
        form = RegistrationForm()
    return render(request, 'registration/contacts.html')

def merch(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/success.html')
    else:
        form = RegistrationForm()
    return render(request, 'registration/merch.html')

def stream(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/success.html')
    else:
        form = RegistrationForm()
    return render(request, 'registration/stream.html')


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id
            })
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]  # Ensures access is only for authenticated users

    def get(self, request):
        # Simulate a response with some user data, ideally fetched from your database
        user_data = {
            "username": request.user.username,
            "email": request.user.email
        }
        return Response(user_data)
def profile_view(request):
    # If you're using a single page application framework:
        return render(request, 'registration/profile.html')
def logout_view(request):
    logout(request)
    return redirect('/home')  # Redirect to home page after logout