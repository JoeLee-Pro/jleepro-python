from django.shortcuts import render
from .models import Card


def home(request):
    cards = Card.featured.all()
    return render(request, 'website/home.html', {'cards': cards})

