from django.db import models
from django.contrib.auth.models import User
# Create your models here.
GENDER_TYPES =(
    ("Male","Male"),
    ("Femal","Female")
)
class UserLibraryAccount(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    gender=models.CharField(max_length=20 ,choices= GENDER_TYPES)
    birthday=models.DateField(null=True,blank=True)
    balance=models.IntegerField(default=0)
    

    def __str__(self):
        return self.user.first_name
    
    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    @property
    def get_username(self):
        return self.user.username

    @property
    def email(self):
        return self.user.email