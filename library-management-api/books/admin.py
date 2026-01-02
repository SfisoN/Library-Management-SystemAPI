from django.contrib import admin
from .models import Book

# Register your models here.

admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'published_date', 'available_copies')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('published_date',)

