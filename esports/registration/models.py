
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

class Team(models.Model):
    name = models.CharField(max_length=100)
    captain = models.ForeignKey(Registrant, on_delete=models.CASCADE)
    # Add more fields as needed

    def __str__(self):
        return self.name
    
class Game(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields as needed

    def __str__(self):
        return self.name