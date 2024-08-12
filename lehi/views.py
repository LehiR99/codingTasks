from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio

def index(request):

    # Home
    home = Home.objects.latest('updated') if Home.objects.exists() else None

    # About
    about = About.objects.latest('updated') if About.objects.exists() else None
    profiles = Profile.objects.filter(about=about) if about else []

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
    }

    return render(request, 'index.html', context)
