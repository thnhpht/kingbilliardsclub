from django import forms
from django.forms import ModelForm
from .models import *


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = "__all__"
       

class DuelForm(ModelForm):
    class Meta:
        model = Duel
        fields = "__all__"
       