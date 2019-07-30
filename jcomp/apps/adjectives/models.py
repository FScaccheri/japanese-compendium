from django.db import models
from django.utils.translation import gettext_lazy as _

from jcomp.apps.common.models import Word


class Adjective(Word):
    group = models.CharField(max_length=5, null=True)

    class Meta:
        verbose_name = _("Adjetivo")
        verbose_name_plural = _("Adjetivos")

    @property
    def type(self):
        return self._meta.verbose_name

    def type_color(self):
        '''
        Bootstrap html class for styling a word row based on its type
        '''
        return "warning"