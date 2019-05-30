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
            'verbs_list': Verb.objects.all(),
            'adjectives_list': Adjective.objects.all(),
        })
        # TODO: this idea is correct but doesn't work
        #  To correct it create method for custom Word model manager
        #  that returns a 'correct' query with all objects (Words, Adjectives, Verbs)
        return context

    # TODO: Create details views
