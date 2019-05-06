from django.urls import re_path
from .views import KanjiListView


urlpatterns = [
    re_path(r'kanji$', KanjiListView.as_view(), name='kanji_list')
]