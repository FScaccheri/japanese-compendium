from django.db import models


class Kanji(models.Model):
    kanji = models.CharField(max_length=50, null=True)
    image = models.ImageField(null=True)
    meaning = models.CharField(max_length=100, null=True)
    strokes_count = models.PositiveIntegerField()
