from django.contrib import admin
from . models import UserLibraryAccount
# Register your models here.

@admin.register(UserLibraryAccount)
class UserlibraryAccountAdmin(admin.ModelAdmin):
    list_display=["user","balance","gender","birthday"]