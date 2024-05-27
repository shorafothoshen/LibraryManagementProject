from django.contrib import admin
from .models import BorrowingModel,ReviewModel
# Register your models here.

@admin.register(BorrowingModel)
class borrowAdmin(admin.ModelAdmin):
    list_display=["borrow_id","book","user","borrowed_date"]

@admin.register(ReviewModel)
class ReviewAdmin(admin.ModelAdmin):
    list_display=["book","name","email","body","date"]
