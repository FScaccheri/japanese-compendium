from django.db import models
from jcomp.apps.common.models import Word


class Adjective(Word):
    group = models.CharField(max_length=5, null=True)

    def type(self):
        return self.__class__.__name__
