from django.shortcuts import render
from django.views.generic.list import ListView
from jcomp.apps.common.models import Word
from jcomp.apps.verbs.models import Verb
from jcomp.apps.adjectives.models import Adjective


class VocabularyListView(ListView):
    model = Word
    paginate_by = 30
    template_name = 'vocabulary_list.html'
    context_object_name = 'words_list'

    def get_context_data(self, **kwargs):
        context = super(VocabularyListView, self).get_context_data(**kwargs)
        context.update({
            'vocabulary_list': Word.objects.vocabulary_list()
        })
        return context
        
    # TODO: Create details views
