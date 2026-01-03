from django.db import models
from django.utils.timezone import now
from books.models import Book
from users.models import User

# Create your models here.

class Checkouts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['book'],
                condition=models.Q(return_date__isnull=True),
                name='unique_active_checkout_per_book'  
            )
        ]

    def __str__(self):
        return f"{self.user} checked out {self.book} on {self.checkout_date}"
