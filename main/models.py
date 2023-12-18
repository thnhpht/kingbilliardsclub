from django.db import models
from datetime import datetime
# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=255, null=True)
    rank = models.CharField(max_length=2, null=True)
    image = models.ImageField(upload_to='images/players', null=True, blank=True)


    def __str__(self):
        return self.name + ' (' + self.rank + ')'
    

class Race(models.Model):
    race = models.IntegerField()


    def __str__(self):
        return str(self.race)

    
class Round(models.Model):
    round = models.CharField(max_length=255)


    def __str__(self):
        return str(self.round)
    
class Table(models.Model):
    table = models.CharField(max_length=2)


    def __str__(self):
        return self.table


class Duel(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE, null=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player1', null=True)
    score1 = models.IntegerField(default=0, null=True, blank=True)
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player2', null=True)
    score2 = models.IntegerField(default=0, null=True, blank=True)
    date = models.DateField(default=datetime.now, null=True)
    time = models.TimeField(null=True)
    live = models.BooleanField(default=False)
    stop_time = models.TimeField(null=True, blank=True)


    class Meta:
        ordering = ['table']


    def __str__(self): 
        return str(self.round) + ': ' + str(self.table) + ' - ' + str(self.player1) + ' - ' + str(self.score1) + ' VS ' + str(self.player2) + ' - ' + str(self.score2) + ' - ' + str(self.date) + ' - ' + str(self.time)
    