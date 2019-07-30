from django.urls import re_path, path
from .views import home_view, WordListCreate


urlpatterns = [
    re_path('^$', home_view, name='home_view'),
    path('api/word/', WordListCreate.as_view()),
]
