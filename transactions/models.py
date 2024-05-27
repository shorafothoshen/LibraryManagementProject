from django.db import models
from accounts.models import UserLibraryAccount
# Create your models here.
class TransactionModel(models.Model):
    account=models.ForeignKey(UserLibraryAccount, on_delete=models.CASCADE, related_name="transaction")
    amount=models.DecimalField(max_digits=12,decimal_places=2)