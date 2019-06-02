from django.shortcuts import render
from django.views.generic.list import ListView
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
    # TODO: Create details views