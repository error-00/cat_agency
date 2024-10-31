from django.shortcuts import render
from rest_framework import generics
from .models import SpyCat
from .serializers import SpyCatSerializer

# List of all cats
class SpyCatList(generics.ListCreateAPIView):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer

    def perform_create(self, serializer):
        serializer.save()


# Getting and updating/deleting specific cat
class SpyCatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer


