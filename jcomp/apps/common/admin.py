from django.contrib import admin
from .models import Word


class WordAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("romaji",)}


admin.site.register(Word, WordAdmin)

