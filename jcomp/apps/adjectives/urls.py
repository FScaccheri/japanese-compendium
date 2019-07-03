from django.urls import re_path, path
from .views import AdjectiveListView, AdjectiveDetailView


urlpatterns = [
    re_path(r'^$', AdjectiveListView.as_view(), name='adjectives_list'),
    path('<slug:slug>', AdjectiveDetailView.as_view(), name='adjective_detail')
]