from django.db import models
from jcomp.apps.kanji.models import Kanji


class Word(models.Model):
    hiragana = models.CharField(max_length=50, blank=True, null=True)
    romaji = models.CharField(max_length=100, blank=True, null=True)
    kanji = models.ForeignKey(Kanji, null=True, blank=True, on_delete=models.CASCADE, related_name='lectures')
    translation = models.CharField(max_length=100, null=True)
    source = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.hiragana

    @property
    def type(self):
        return self.__class__.__name__.lower()

    def type_color(self):
        '''
        Bootstrap html class for styling a word row based on its type
        '''
        return "table-secondary"
