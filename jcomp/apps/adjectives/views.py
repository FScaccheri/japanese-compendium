from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Adjective


class AdjectiveListView(ListView):
    model = Adjective
    paginate_by = 50
    template_name = 'adjective_list.html'
    context_object_name = 'adjectives_list'


class AdjectiveDetailView(DetailView):
    model = Adjective
    template_name = 'adjective_detail.html'
    context_object_name = 'adjective'
