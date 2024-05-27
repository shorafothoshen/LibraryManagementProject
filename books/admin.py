from django.contrib import admin
from .models import BookModel
# Register your models here.

@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name","price")}
    list_display=["name","author","category","price","slug"]