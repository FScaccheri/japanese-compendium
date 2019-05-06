from django.urls import re_path
from .views import VocabularyListView


urlpatterns = [
    re_path(r'vocabulary$', VocabularyListView.as_view(), name='vocabulary_list')
]