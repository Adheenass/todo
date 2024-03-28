#from django.shortcuts import render

# Create your views here.
# GET POST UPDATE DELETE
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer


class TodoGetCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer