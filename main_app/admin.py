from django.contrib import admin
# import your models here
from .models import Emu, Feeding

# Register your models here
admin.site.register(Emu)
admin.site.register(Feeding)