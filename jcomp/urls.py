"""jcomp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.common, name='common')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='common')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('jcomp.apps.common.urls')),
    re_path(r'^vocabulary/', include('jcomp.apps.vocabulary.urls')),
    re_path(r'^verbs/', include('jcomp.apps.verbs.urls')),
    re_path(r'^adjectives/', include('jcomp.apps.adjectives.urls')),
    re_path(r'^kanji/', include('jcomp.apps.kanji.urls')),
    re_path(r'^search/', include('haystack.urls')),
    path('frontend/', include('jcomp.apps.frontend.urls'))
]
