from django.contrib import admin
from .models import User, Location, Creature

admin.register(User)
admin.register(Location)
admin.register(Creature)