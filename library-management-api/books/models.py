from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"