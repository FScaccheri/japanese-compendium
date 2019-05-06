from django.urls import re_path
from .views import AdjectiveListView


urlpatterns = [
    re_path(r'adjectives$', AdjectiveListView.as_view(), name='adjectives_list')
]