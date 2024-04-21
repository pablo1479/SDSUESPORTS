from django.db import models

class ESportsTeam(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()