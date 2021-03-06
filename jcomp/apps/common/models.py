import romkan
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from jcomp.apps.kanji.models import Kanji


class WordManager(models.Manager):
    # Man this is some fucked up shit right here
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
        
        #full_list.reverse()
        return full_list


class Word(models.Model):
    hiragana = models.CharField(max_length=50, blank=True, null=True)
    romaji = models.CharField(max_length=100, blank=True, null=True)
    kanji = models.ForeignKey(Kanji, null=True, blank=True, on_delete=models.CASCADE, related_name='lectures')
    translation = models.CharField(max_length=100, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(default="slug")

    objects = WordManager()

    class Meta:
        verbose_name = _("Palabra")
        verbose_name_plural = _("Palabras")
        ordering = ['-id']

    def __str__(self):
        return self.hiragana

    def clean(self):
        if not self.hiragana:
            self.hiragana = romkan.to_hiragana(self.romaji)
        elif not self.romaji:
            self.romaji = romkan.to_roma(self.hiragana).capitalize()
        elif not self.hiragana and not self.romaji:
            raise ValidationError("You have to enter either the Hiragana or Romaji of a Word")

        self.slug = slugify(self.romaji)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Word, self).save(*args, **kwargs)

    @property
    def type(self):
        return self._meta.verbose_name

    def type_color(self):
        '''
        Bootstrap html class for styling a word row based on its type
        '''
        return "primary"
