from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Location)
admin.site.register(Creature)
admin.site.register(FightLog)