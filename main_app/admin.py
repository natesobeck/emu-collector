from django.contrib import admin
# import your models here
from .models import Emu, Feeding, BowTie

# Register your models here
admin.site.register(Emu)
admin.site.register(Feeding)
admin.site.register(BowTie)