from django.shortcuts import render
from .forms import RegistrationForm

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
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def application(request):
    return render(request, 'application.html')

def stats(request):
    return render(request, 'stats.html')

def contact(request):
    return render(request, 'contact.html')

def merch(request):
    return render(request, 'merch.html')

def stream(request):
    return render(request, 'stream.html')
