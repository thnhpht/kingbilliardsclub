from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('live-scores/', views.liveScores, name="livescores"),
    path('bracket/', views.bracket, name="bracket"),
    path('login/', views.login, name="login"),
]