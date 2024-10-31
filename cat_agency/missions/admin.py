from django.contrib import admin
from .models import Target, Mission


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "complete")


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ("cat", "complete")
