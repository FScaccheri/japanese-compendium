from haystack import indexes
from .models import Word


class WordIndex(indexes.ModelSearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Word

    def index_queryset(self, using=None):
        return self.get_model.objects.all()