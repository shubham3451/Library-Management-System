from django.contrib import admin
from .models import Book, Member

# Register the Book model to be managed via the admin interface
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

# Register the Member model to be managed via the admin interface
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'membership_date')
    search_fields = ('name', 'email')

# Register the models with the admin site
admin.site.register(Book, BookAdmin)
admin.site.register(Member, MemberAdmin)

