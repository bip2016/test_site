from django.shortcuts import render
from django.shortcuts import render, redirect


def index(request):
    title = "Атмосферное элекстричество"
    return render(request, 'atmospheric_electricity.html', {'title': title})


