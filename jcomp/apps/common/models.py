from itertools import chain
from django.db import models
from django.db.models import Q
from jcomp.apps.kanji.models import Kanji


class WordManager(models.Manager):
    # Man this some fucked up shit right here
    def vocabulary_list(self):
        from jcomp.apps.verbs.models import Verb
        from jcomp.apps.adjectives.models import Adjective

        words = list(Word.objects.filter(
            verb__isnull=True,
            adjective__isnull=True))
        verbs = list(Verb.objects.all())
        adjectives = list(Adjective.objects.all())

        verbs_list = [verb.hiragana for verb in verbs]
        adjectives_list = [adjective.hiragana for adjective in adjectives]
        
        full_list = words.copy()
        for word in words:
            index = words.index(word)
            if word.hiragana in verbs_list:
                full_list[index] = Verb.objects.get(hiragana=word.hiragana)
            if word.hiragana in adjectives_list:
                full_list[index] = Adjective.objects.get(hiragana=word.hiragana)
        
        full_list.reverse()
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
        return "table-primary"
