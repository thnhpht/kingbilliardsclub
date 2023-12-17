from django import forms
from django.forms import ModelForm
from .models import *
from django.utils.translation import gettext_lazy as _

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control input mb-2'}),
            'rank': forms.TextInput(attrs={'class': 'form-control input mb-2'}),
            'image': forms.FileInput(attrs={'class': 'form-control input mb-2', 'required': False})
        }

        labels = {
            "name": _("Tên người chơi"),
            "rank": _("Hạng"),
            "image": _("Hình ảnh"),
        }


class DuelForm(ModelForm):
    class Meta:
        model = Duel
        fields = "__all__"
       