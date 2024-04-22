from django.shortcuts import render
from .forms import RegistrationForm
from .serializers import PlayerSerializer, TeamSerializer
from rest_framework import generics
from .models import Player, Team

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
def teamstats(request):
    teamStats = {
        'manshawdies': {
            'game1': { 'name': 'Valorant', 'wins': 5, 'losses': 3, 'draws': 2, 'playerData': [] },
            'game2': { 'name': 'Overwatch 2', 'wins': 7, 'losses': 1, 'draws': 4, 'playerData': [] }
        },
        'tehs-angels': {
            'game1': { 'name': 'League of Legends', 'wins': 3, 'losses': 5, 'draws': 1, 'playerData': [] },
            'game2': { 'name': 'Smite', 'wins': 6, 'losses': 2, 'draws': 3, 'playerData': [] }
        },
        'doganators': {
            'game1': { 'name': 'Forza Horizon', 'wins': 4, 'losses': 4, 'draws': 2, 'playerData': [
                { 'name': 'Papa Pookie', 'stats': [12, 18, 20, 25] },
                { 'name': 'Robert McRizztock', 'stats': [11, 17, 19, 23] },
                { 'name': 'Alex Rivera', 'stats': [14, 21, 25, 31] },
                { 'name': 'PookieBear Pablo', 'stats': [10, 15, 18, 22] }
            ] },
            'game2': { 'name': 'Gran Turismo', 'wins': 8, 'losses': 0, 'draws': 2, 'playerData': [] }
        },
        'astrofees': {
            'game1': { 'name': 'Math is Fun', 'wins': 6, 'losses': 2, 'draws': 2, 'playerData': [] },
            'game2': { 'name': 'Poptropica', 'wins': 4, 'losses': 4, 'draws': 3, 'playerData': [] }
        }
    }

    selectedGame = 'game1'  # default to game1, you can adjust this based on your requirements

    # Pass teamStats and selectedGame to the template
    return render(request, 'registration/stats.html', {'teamStats': teamStats, 'selectedGame': selectedGame})

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

class PlayerList(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class TeamList(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

