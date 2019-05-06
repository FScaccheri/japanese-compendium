from django.contrib import admin
from .models import Kanji


class KanjiAdmin(admin.ModelAdmin):
    fields = ['kanji', 'image', 'meaning', 'strokes_count']


admin.site.register(Kanji, KanjiAdmin)
