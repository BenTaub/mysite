from django.contrib import admin
from .models import Publisher, Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date',)  # What fields will be displayed in list
    list_filter = ('publication_date', 'publisher', )  # What fields appear in filter box on right
    date_hierarchy = 'publication_date'  # What date field to use as drill down at top of form
    ordering = ('-publication_date',)  # Ordering the list
    # fields = ('title', 'publisher', 'authors', 'publication_date')  # What fields will appear on data entry form
    filter_horizontal = ('authors',)  # Adds cool way to select multiple authors (i.e. M:N options)
    raw_id_fields = ('publisher',)  # Add data as its key, not its decoded value

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
