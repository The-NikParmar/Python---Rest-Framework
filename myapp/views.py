from django.shortcuts import render
from rest_framework import generics
from .models import *
from .seriazlizers import BookSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()  # Corrected line
    serializer_class = BookSerializer
