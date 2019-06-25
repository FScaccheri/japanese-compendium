from django.db import models
from jcomp.apps.common.models import Word


class Adjective(Word):
    group = models.CharField(max_length=5, null=True)

    def type(self):
        return self.__class__.__name__

    def type_color(self):
        '''
        Bootstrap html class for styling a word row based on its type
        '''
        return "warning"