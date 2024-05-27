from django import forms
from .models import UserLibraryAccount
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

GENDER_TYPES =(
    ("Male","Male"),
    ("Female","Female"),
)


class SignUpForm(UserCreationForm):
    gender=forms.ChoiceField(choices= GENDER_TYPES)
    birthday=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))

    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2","gender","birthday"]

    def save(self, commit=True):
        user=super().save(commit=False)
        if commit:
            user.save()
            gender=self.cleaned_data.get("gender")
            birthday=self.cleaned_data.get("birthday")

            UserLibraryAccount.objects.create(
                user=user,
                gender=gender,
                birthday=birthday,
            )

            return user
        
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                "class":'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500'
            })

class UpdateForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_TYPES)
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

    class Meta:
        model = User
        fields =["first_name","last_name",'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                "class":'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500'
            })
        

        if self.instance:
            try:
                user_account = UserLibraryAccount.objects.get(user=self.instance)
            except UserLibraryAccount.DoesNotExist:
                user_account = None
            if user_account:
                self.fields['gender'].initial = user_account.gender
                self.fields['birthday'].initial = user_account.birthday

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_account, created = UserLibraryAccount.objects.get_or_create(user=user)
            user_account.gender = self.cleaned_data['gender']
            user_account.birthday = self.cleaned_data['birthday']

            user_account.save()
        return user