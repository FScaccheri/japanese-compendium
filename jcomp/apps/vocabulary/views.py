from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from jcomp.apps.common.models import Word
from jcomp.apps.verbs.models import Verb
from jcomp.apps.adjectives.models import Adjective


class VocabularyListView(ListView):
    model = Word
    paginate_by = 50
    template_name = 'vocabulary_list.html'
    context_object_name = 'words_list'

    def get_queryset(self):
        return Word.objects.vocabulary_list()


class WordDetailView(DetailView):
    model = Word 
    template_name = 'word_detail.html'
    context_object_name = 'word'