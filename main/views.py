from django.shortcuts import render
from .models import *
from datetime import datetime
from django.http import JsonResponse

# Create your views here.


def home(request):
    return render(request, 'main.html')


def login(request):
    return render(request, 'login.html')


def liveScores(request):
    pk = ""
    action = "stop"

    if request.method == 'POST':
        pk = request.POST["pk"]
        if request.POST["action"] == "start":
            action = "start"
        else:
            Duel.objects.filter(pk=pk).update(stop_time=datetime.now().strftime('%H:%M:%S'))

    duels = Duel.objects.all()
    context = {'duels': duels,
            'pk': pk,
            'action': action
            }
            
    return render(request, 'live-scores.html', context)


def bracket(request):
    return render(request, 'bracket.html')

