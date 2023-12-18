from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('live-scores/', views.liveScores, name="live_scores"),
    path('bracket/', views.bracket, name="bracket"),
    path('sign-in/', views.signIn, name="sign_in"),
    path('sign-out/', views.signOut, name='sign_out'),
    path('player/', views.player, name='player'),
    path('duel/', views.duel, name='duel'),
]