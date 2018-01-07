from django.contrib import admin
from .models import (
    Snippet
)
from django.contrib.auth.models import User

# Register your models here.


class SnippetInline(admin.TabularInline):
    model = Snippet


class PersonAdmin(admin.ModelAdmin):
    inlines = [
        User
    ]
admin.site.register(Snippet)
