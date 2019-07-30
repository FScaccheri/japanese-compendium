from django.db import models
from django.utils.translation import gettext_lazy as _

from jcomp.apps.common.models import Word


class Verb(Word):
    group = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = _("Verbo")
        verbose_name_plural = _("Verbos")

    @property
    def type(self):
        return self._meta.verbose_name

    def type_color(self):
        '''
        Bootstrap html class for styling a word row based on its type
        '''
        return "danger"
