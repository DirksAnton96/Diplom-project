from django.contrib import admin

from django.db.models import QuerySet, F

from .models import PlaceCoworking, UsersCoworking

# Register your models here.
@admin.register(PlaceCoworking)
class PlaceCoworkingAdmin(admin.ModelAdmin):
    list_display = ["name","description","created_at","mode_time"]
    date_hierarchy = "created_at"

@admin.register(UsersCoworking)
class UsersCoworkingAdmin(admin.ModelAdmin):
    pass