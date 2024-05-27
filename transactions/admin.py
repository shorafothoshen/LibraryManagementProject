from django.contrib import admin
from . models import TransactionModel
# Register your models here.
@admin.register(TransactionModel)
class TransactionAdmin(admin.ModelAdmin):
    list_display=["account","amount"]