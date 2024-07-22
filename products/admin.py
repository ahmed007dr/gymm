from django.contrib import admin
from .models import Gym , Brand ,GymImages


class GymImagesInline(admin.TabularInline):
    model = GymImages

class GymAdmin(admin.ModelAdmin):
    inlines = [GymImagesInline]

admin.site.register(Gym,GymAdmin)
admin.site.register(Brand)
admin.site.register(GymImages)
