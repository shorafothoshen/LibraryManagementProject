from django.contrib import admin
from .models import CategoryModel
# Register your models here.

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":('category_name',)}
    list_display=["category_name","slug"]