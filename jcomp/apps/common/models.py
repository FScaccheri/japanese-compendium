from itertools import chain
from django.db import models
from jcomp.apps.kanji.models import Kanji


class WordManager(models.Manager):
    def vocabulary_list(self):
        from jcomp.apps.verbs.models import Verb
        from jcomp.apps.adjectives.models import Adjective

        verbs = Verb.objects.all()
        adjectives = Adjective.objects.all()

        verbs_list = [verb.hiragana for verb in verbs]
        adjectives_list = [adjective.hiragana for adjective in adjectives]
        words = Word.objects.exclude(hiragana__in=(verbs_list + adjectives_list))

        full_list = list(chain(words, verbs, adjectives))
        return full_list


class Word(models.Model):
    hiragana = models.CharField(max_length=50, blank=True, null=True)
    romaji = models.CharField(max_length=100, blank=True, null=True)
    kanji = models.ForeignKey(Kanji, null=True, blank=True, on_delete=models.CASCADE, related_name='lectures')
    translation = models.CharField(max_length=100, null=True)
    source = models.CharField(max_length=50, null=True)

    objects = WordManager()

    def __str__(self):
        return self.hiragana

    @property
    def type(self):
        return self.__class__.__name__

    def type_color(self):
        '''
        Bootstrap html class for styling a word row based on its type
        '''
        return "table-secondary"
