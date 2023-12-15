from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.hashers import check_password
# Create your views here.

User = get_user_model()
def home(request):
    return render(request, 'main.html')


def authenticateUser(email=None, password=None):
    try:
        user = User.objects.get(email=email)

        if check_password(password, user.password):
            return user
        return None
    except User.DoesNotExist:
        return None
    

def signIn(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticateUser(email, password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Đăng nhập thành công')
            return redirect('/home/')
        else:
            messages.warning(request, 'Email hoặc mật khẩu không chính xác')
    return render(request, 'login.html')


def signOut(request):
    logout(request)
    messages.success(request, 'Đăng xuất thành công')
    return redirect('/home/')


def liveScores(request):
    if request.method == 'POST':
        pk = request.POST["pk"]
        if request.POST["action"] == "start":
            Duel.objects.filter(pk=pk).update(live=True)
        elif request.POST["action"] == "stop":
            Duel.objects.filter(pk=pk).update(live=False)
            Duel.objects.filter(pk=pk).update(stop_time=datetime.now().strftime('%H:%M:%S'))

    duels = Duel.objects.all()
    rounds = Round.objects.all().order_by('pk').values()
    for duel in duels:
        print(duel)
    context = {'duels': duels,
               'rounds': rounds,
            }
            
    return render(request, 'live-scores.html', context)


def bracket(request):
    return render(request, 'bracket.html')


def createPlayer(request):
    context = {}
 
    form = PlayerForm(request.POST or None, request.FILES or None)
     
    if form.is_valid():
        form.save()
        return redirect('/create-player/')
 
    context['form']= form
    return render(request, 'create-player.html', context)


def createDuel(request):
    context = {}
 
    form = DuelForm(request.POST or None, request.FILES or None)
     
    if form.is_valid():
        form.save()
        return redirect('/create-duel/')
 
    context['form']= form
    return render(request, 'create-duel.html', context)


