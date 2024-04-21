from django.db import models

class Registrant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    password = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    twitch = models.CharField(max_length=100, blank=True, null=True)

