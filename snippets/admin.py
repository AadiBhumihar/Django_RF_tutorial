from django.contrib import admin
from .models import (
    Snippet,
    
)

# Register your models here.


class SnippetInline(admin.TabularInline):
    model = Snippet


class PersonAdmin(admin.ModelAdmin):
    inlines = [
        SnippetInline
    ]
admin.site.register(Snippet)
#admin.site.register(Person,PersonAdmin)