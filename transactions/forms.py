from django import forms
from .models import TransactionModel

class DepositForm(forms.ModelForm):
    class Meta:
        model=TransactionModel
        fiels=["amount"]
        exclude = ['account']
    
    def clean_amount(self):
        min_deposit_amount = 0
        amount = self.cleaned_data.get('amount')
        if amount < min_deposit_amount:
            raise forms.ValidationError(f'Your deposit amount must be positive $')
        return amount
    