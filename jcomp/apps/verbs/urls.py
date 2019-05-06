from django.urls import re_path
from .views import VerbListView


urlpatterns = [
    re_path(r'verbs$', VerbListView.as_view(), name='verbs_list')
]