from django.db import models
from category.models import CategoryModel
# Create your models here.
class BookModel(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    category=models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    description=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to="books/media/image/", blank=True, null=True)
    slug=models.SlugField(max_length=100, unique=True ,blank= True,null=True)

    def __str__(self):
        return self.name
