from django.db import models
from books.models import Book
from users.models import User

# Create your models here.

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} checked out {self.book} on {self.checkout_date}"
