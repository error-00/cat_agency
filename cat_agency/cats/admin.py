from django.contrib import admin
from .models import SpyCat

@admin.register(SpyCat)
class SpyCatAdmin(admin.ModelAdmin):
    list_display = ('name', 'years_of_experience', 'breed', 'salary')
