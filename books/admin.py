from django.contrib import admin
from .models import Book


# Register your models here.
admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','description','published_date']
    list_display_links = ('title',)
    list_editable = ('is_published',)
    search_fields = ['title']
    list_filter = ('author', 'published_date')
    ordering = ('-published_date',)

fieldsets = (
    ("Book Information", {
        "fields": ("title", "author")
    }),
    ("Publication Details", {
        "fields": ("published_date", "is_published")
    }),
    ("Description", {
        "fields": ("description",)
    }),
)
