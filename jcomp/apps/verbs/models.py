from django.db import models
from jcomp.apps.common.models import Word


class Verb(Word):
    group = models.PositiveIntegerField(null=True, blank=True)

    @property
    def type(self):
        return self.__class__.__name__.lower()

    @property
    def detail_url(self):
        return self.type + "_detail"

    def type_color(self):
        '''
        Bootstrap html class for styling a word row based on its type
        '''
        return "danger"
