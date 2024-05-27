from django.shortcuts import render
from .models import TransactionModel
from .forms import DepositForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib import messages
from Library_management.views import send_email

# Create your views here.
class DepositView(LoginRequiredMixin, CreateView):
    model = TransactionModel
    form_class = DepositForm
    template_name = 'transaction/deposit.html'
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        transaction = form.save(commit=False)
        transaction.account = account
        transaction.save()
        account.balance += amount
        account.save(update_fields=['balance'])
        messages.success(self.request,f"You Successfully deposit is $ {amount} ✅")
        send_email("Deposit Money","transaction/deposit_email.html",self.request.user,amount)
        return super().form_valid(form)