from django.urls import re_path, path
from .views import VocabularyListView, WordDetailView


urlpatterns = [
    re_path(r'^$', VocabularyListView.as_view(), name='vocabulary_list'),
    re_path(r'^(?P<slug>\w+)/$', WordDetailView.as_view(), name='word_detail')
]