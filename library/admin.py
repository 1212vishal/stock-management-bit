from django.contrib import admin
from .models import Book,studentExtra,IssuedBook
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)


class studentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(studentExtra, studentExtraAdmin)


class IssuedBookAdmin(admin.ModelAdmin):
    pass
admin.site.register(IssuedBook, IssuedBookAdmin)
