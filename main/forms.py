from django import forms
from django.forms import ModelForm
from .models import *
from django.utils.translation import gettext_lazy as _

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'rank': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'image': forms.FileInput(attrs={'class': 'form-control mb-2', 'required': False})
        }

        labels = {
            "name": _("Tên người chơi"),
            "rank": _("Hạng"),
            "image": _("Hình ảnh"),
        }


class DuelForm(ModelForm):
    class Meta:
        model = Duel
        fields = ('round', 'table', 'player1', 'score1', 'player2', 'score2', 'date', 'time')

        widgets = {
                'round': forms.Select(attrs={'class': 'form-control mb-2'}),
                'table': forms.Select(attrs={'class': 'form-control mb-2'}),
                'player1': forms.Select(attrs={'class': 'form-control mb-2'}),
                'score1': forms.NumberInput(attrs={'class': 'form-control mb-2', 'required': False}),
                'player2': forms.Select(attrs={'class': 'form-control mb-2'}),
                'score2': forms.NumberInput(attrs={'class': 'form-control mb-2', 'required': False}),
                'date': forms.SelectDateWidget(attrs={'class': 'form-control mb-2 d-inline w-33'}),
                'time': forms.TimeInput(attrs={'class': 'form-control mb-2'}),
            }

        labels = {
            "round": _("Vòng đấu"),
            "table": _("Bàn"),
            "player1": _("Người chơi 1"),
            "score1": _("Điểm người chơi 1"),
            "player2": _("Người chơi 2"),
            "score2": _("Điểm người chơi 2"),
            "date": _("Ngày đấu"),
            "time": _("Giờ đấu"),
        }
        
