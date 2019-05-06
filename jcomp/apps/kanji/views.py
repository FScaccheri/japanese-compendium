from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Kanji


class KanjiListView(ListView):
    model = Kanji
    paginate_by = 50
    template_name = 'kanji_list.html'
