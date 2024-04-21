from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Registrant

@receiver(post_save, sender=Registrant)
def registrant_created(sender, instance, created, **kwargs):
    if created:
        # Here you can perform additional actions when a new Registrant is created,
        # such as sending a welcome email or creating related objects
        
        # For example, let's print a message when a new Registrant is created
        print(f"New Registrant created: {instance}")
