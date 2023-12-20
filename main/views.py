from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.hashers import check_password


User = get_user_model()
def home(request):
    return render(request, 'home.html')


# Auth
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
            return redirect('/')
        else:
            messages.warning(request, 'Email hoặc mật khẩu không chính xác')
    return render(request, 'auth/login.html')


def signOut(request):
    logout(request)
    messages.success(request, 'Đăng xuất thành công')
    return redirect('/')


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


def contact(request):
    return render(request, 'contact.html')


def player(request):
    action = ""
    form = PlayerForm()
    players = Player.objects.all()

    if request.method == "POST":
        data = request.POST
        action = data.get("action")
        if action == "search":
            search = request.POST.get('search-words')
            players = Player.objects.filter(name__contains=search)
        
    context = {'players': players,
               'action': action,
               'form': form}
    return render(request, 'player.html', context)


# Admin
def managePlayer(request):
    pk = ""
    action = ""
    form = PlayerForm()
    players = Player.objects.all()

    if request.method == "POST":
        data = request.POST
        action = data.get("action")
        if action == "search":
            search = request.POST.get('search-words')
            players = Player.objects.filter(name__contains=search)
        elif action == "create":   
            form_create = PlayerForm(request.POST, request.FILES)
            if form_create.is_valid():
                form_create.save()  
                return redirect('/manage-player/')
        elif action == "show-edit-form":
            pk = request.POST.get("pk")
            player = Player.objects.get(id=pk)
            form = PlayerForm(instance=player)
        elif action == "edit":
            pk = request.POST.get("pk")
            player = Player.objects.get(id=pk)
            form_edit = PlayerForm(request.POST, request.FILES, instance=player)
            if form_edit.is_valid():
                form_edit.save()  
                return redirect('/manage-player/')
        elif action == "delete":
            player = Player.objects.get(id=request.POST.get("pk"))
            player.delete()
            return redirect('/manage-player/')
    
    context = {'players': players,
               'pk': pk,
               'action': action,
               'form': form}
    return render(request, 'admin/manage-player.html', context)


def manageDuel(request):
    pk = ""
    action = ""
    form = DuelForm()
    duels = Duel.objects.all()

    if request.method == "POST":
        data = request.POST
        action = data.get("action")
    
        if action == "create":   
            form_create = DuelForm(request.POST)
            if form_create.is_valid():
                form_create.save()  
                return redirect('/manage-duel/')
        elif action == "show-edit-form":
            pk = request.POST.get("pk")
            duel = Duel.objects.get(id=pk)
            form = DuelForm(instance=duel)
        elif action == "edit":
            pk = request.POST.get("pk")
            duel = Duel.objects.get(id=pk)
            form_edit = DuelForm(request.POST, instance=duel)
            if form_edit.is_valid():
                form_edit.save()  
                return redirect('/manage-duel/')
        elif action == "delete":
            duel = Duel.objects.get(id=request.POST.get("pk"))
            duel.delete()
            return redirect('/manage-duel/')
        elif action == "up-score1":
            pk = request.POST.get("pk")
            Duel.objects.filter(pk=pk).update(score1=int(request.POST["score1"]) + 1)
            return redirect('/manage-duel/')
        elif action == "down-score1":
            pk = request.POST.get("pk")
            Duel.objects.filter(pk=pk).update(score1=int(request.POST["score1"]) - 1)
            return redirect('/manage-duel/')
        elif action == "up-score2":
            pk = request.POST.get("pk")
            Duel.objects.filter(pk=pk).update(score2=int(request.POST["score2"]) + 1)
            return redirect('/manage-duel/')
        elif action == "down-score2":
            pk = request.POST.get("pk")
            Duel.objects.filter(pk=pk).update(score2=int(request.POST["score2"]) - 1)
            return redirect('/manage-duel/')
        
    context = {'duels': duels,
               'pk': pk,
               'action': action,
               'form': form}
    return render(request, 'admin/manage-duel.html', context)


def manageRound(request):
    pk = ""
    action = ""
    form = RoundForm()
    rounds = Round.objects.all()

    if request.method == "POST":
        data = request.POST
        action = data.get("action")
    
        if action == "create":   
            form_create = RoundForm(request.POST)
            if form_create.is_valid():
                form_create.save()  
                return redirect('/manage-round/')
        elif action == "show-edit-form":
            pk = request.POST.get("pk")
            round = Round.objects.get(id=pk)
            form = RoundForm(instance=round)
        elif action == "edit":
            pk = request.POST.get("pk")
            round = Round.objects.get(id=pk)
            form_edit = RoundForm(request.POST, instance=round)
            if form_edit.is_valid():
                form_edit.save()  
                return redirect('/manage-round/')
        elif action == "delete":
            round = Round.objects.get(id=request.POST.get("pk"))
            round.delete()
            return redirect('/manage-round/')
        
        
    context = {'rounds': rounds,
               'pk': pk,
               'action': action,
               'form': form}
    return render(request, 'admin/manage-round.html', context)