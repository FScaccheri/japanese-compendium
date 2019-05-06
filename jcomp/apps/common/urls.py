from django.urls import re_path
from .views import home_view


urlpatterns = [
    re_path('^$', home_view, name='home_view')
]
