from django.shortcuts import render
from django.views.generic.list import ListView
from jcomp.apps.common.models import Word


class VocabularyListView(ListView):
    model = Word
    paginate_by = 300
    template_name = 'vocabulary_list.html'

    # TODO: Create details views
