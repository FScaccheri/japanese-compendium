from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Adjective


class AdjectiveListView(ListView):
    model = Adjective
    paginate_by = 50
    template_name = 'adjective_list.html'
