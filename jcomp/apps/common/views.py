from django.shortcuts import render, HttpResponse
from .models import Word
from .serializers import WordSerializer
from rest_framework import generics

def home_view(request):
    return render(request, 'home.html')


class WordListCreate(generics.ListCreateAPIView):
    queryset = Word.objects.vocabulary_list()
    serializer_class = WordSerializer
