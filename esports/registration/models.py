
from django.db import models

class Registrant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    password = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    twitch = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Player(models.Model):
    registrant = models.OneToOneField(Registrant, on_delete=models.CASCADE)
    # Add fields for player stats
    kills = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    # Add more fields as needed

    def __str__(self):
        return self.registrant.first_name

class Team(models.Model):
    name = models.CharField(max_length=100)
    captain = models.ForeignKey(Registrant, on_delete=models.CASCADE)
    players = models.ManyToManyField(Player)  # Many-to-many relationship with Player model
    # Add fields for team stats
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    # Add more fields as needed

    def __str__(self):
        return self.name
    
class Game(models.Model):
    name = models.CharField(max_length=100)
    teams = models.ManyToManyField(Team)  # Many-to-many relationship with Team model
    # Add more fields as needed

    def __str__(self):
        return self.name