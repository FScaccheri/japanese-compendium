from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .utils import VerbConjugator
from .models import Verb


class VerbListView(ListView):
    model = Verb
    paginate_by = 50
    template_name = 'verb_list.html'
    context_object_name = 'verbs_list'


class VerbDetailView(DetailView):
    model = Verb 
    template_name = 'verb_detail.html'
    context_object_name = 'verb'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["conjugator"] = VerbConjugator(context["verb"])
        return context
