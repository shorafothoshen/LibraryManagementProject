from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import FormView,ListView,View
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView,LogoutView
from borrow.models import BorrowingModel
from .models import UserLibraryAccount
from django.contrib import messages
from Library_management.views import send_email
# Create your views here.

class SignUpClassView(FormView):
    template_name="accounts/signup.html"
    form_class=forms.SignUpForm
    success_url=reverse_lazy("Home")

    def form_valid(self, form):
        user=form.save()
        login(self.request, user)
        messages.success(self.request,"Successfully Signin Your account ✅")
        send_email("Account Create Successfully","accounts/account_email.html",self.request.user,0)
        return super().form_valid(form)

class LoginClassView(LoginView):
    template_name="accounts/login.html"
    def get_success_url(self):
        messages.success(self.request, "Successfully Logged in ✅")
        send_email("Log In","accounts/login_email.html",self.request.user,0)
        return reverse_lazy("Home")

class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('Home')
    
class Profileview(ListView):
    model=BorrowingModel
    template_name="accounts/profile.html"
    context_object_name="borrow_history"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["borrow_history"]=BorrowingModel.objects.filter(user=self.request.user)
        context["User"]=self.request.user
        return context

class UpdateViewClass(View):
    template_name = 'accounts/profile_update.html'

    def get(self, request):
        form = forms.UpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = forms.UpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(self.request,"Your Account Successfully Updateded ✅")
            send_email("Profile Update","accounts/update_email.html",self.request.user,0)
            return redirect('Profile')
        else:
            messages.error(self.request,"Wrong Informations ❌")
        return render(request, self.template_name, {'form': form})

