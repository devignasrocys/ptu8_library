from django.contrib import admin
from . import models

class BookAdmin(admin.ModelAdmin):
    list_display = ("author", "title")

# Register your models here.
admin.site.register(models.Genre)
admin.site.register(models.Author)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.BookInstance)