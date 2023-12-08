from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=255, null=True)
    rank = models.CharField(max_length=2, null=True)


    def __str__(self):
        return self.name + ' (' + self.rank + ')'
    

class Race(models.Model):
    race = models.IntegerField()


    def __str__(self):
        return str(self.race)

class Race(models.Model):
    race = models.IntegerField()


    def __str__(self):
        return str(self.race)
    
    
class Table(models.Model):
    table = models.CharField(max_length=2)


    def __str__(self):
        return self.table


class Duel(models.Model):
    table = models.OneToOneField(Table, on_delete=models.CASCADE, null=True, blank=True)
    player1 = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='player1', null=True, blank=True)
    score1 = models.IntegerField()
    player2 = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='player2', null=True, blank=True)
    score2 = models.IntegerField()
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    stop_time = models.TimeField(null=True, blank=True)


    def __str__(self): 
        return str(self.table) + ': ' + str(self.player1) + ' - ' + str(self.score1) + ' VS ' + str(self.player2) + ' - ' + str(self.score2) + ' - ' + str(self.date) + ' - ' + str(self.time)