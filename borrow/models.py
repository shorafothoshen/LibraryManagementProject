from django.db import models
from books.models import BookModel
from django.contrib.auth.models import User
# Create your models here.
class BorrowingModel(models.Model):
    borrow_id=models.IntegerField(primary_key=True)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book.name
    
class ReviewModel(models.Model):
    book=models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name="reviews")
    name=models.CharField(max_length=100)
    email=models.EmailField()
    body=models.TextField()
    date=models.DateField(auto_now_add=True)