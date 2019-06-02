from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Verb


class VerbListView(ListView):
    model = Verb
    #paginate_by = 50
    template_name = 'verb_list.html'
