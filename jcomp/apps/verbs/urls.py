from django.urls import re_path, path
from .views import VerbListView, VerbDetailView


urlpatterns = [
    re_path(r'^$', VerbListView.as_view(), name='verbs_list'),
    path('<slug:slug>', VerbDetailView.as_view(), name='verb_detail')
]