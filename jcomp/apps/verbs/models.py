from django.db import models
from jcomp.apps.common.models import Word


class Verb(Word):
    group = models.PositiveIntegerField(null=True, blank=True)

    def type(self):
        return self.__class__.__name__
