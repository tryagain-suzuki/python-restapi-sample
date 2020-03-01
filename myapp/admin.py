from django.contrib import admin

# Register your models here.
from .models import User, Book


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass