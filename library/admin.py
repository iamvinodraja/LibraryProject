# admin.py
# Put this file in your library app folder

from django.contrib import admin
from .models import Author, Book, Member, BorrowRecord


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'bio']
    search_fields = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'total_copies', 'available_copies']
    search_fields = ['title', 'isbn']
    list_filter = ['author']


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'membership_date']
    search_fields = ['name', 'email']


@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ['book', 'member', 'borrow_date', 'return_date']
    list_filter = ['borrow_date', 'return_date']
    search_fields = ['book__title', 'member__name']
