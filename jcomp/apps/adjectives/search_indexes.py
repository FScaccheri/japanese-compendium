from haystack import indexes
from .models import Adjective


class WordIndex(indexes.ModelSearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Adjective

    def index_queryset(self, using=None):
        return self.get_model().objects.all()