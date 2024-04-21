from django.contrib import admin
from .models import Registrant, Team, Game  # Import the models you want to register with the admin site

# Register your models with the admin site
admin.site.register(Registrant)
admin.site.register(Team)
admin.site.register(Game)


