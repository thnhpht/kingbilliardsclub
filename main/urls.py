from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('live-scores/', views.liveScores, name="live_scores"),
    path('bracket/', views.bracket, name="bracket"),
    path('contact/', views.contact, name="contact"),
    path('sign-in/', views.signIn, name="sign_in"),
    path('sign-out/', views.signOut, name='sign_out'),
    path('player/', views.player, name='player'),
    path('manage-player/', views.managePlayer, name='manage_player'),
    path('manage-duel/', views.manageDuel, name='manage_duel'),
    path('manage-round/', views.manageRound, name='manage_round'),
]