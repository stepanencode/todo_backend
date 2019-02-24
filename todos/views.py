from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


@api_view(['GET'])
def radio(request):
    return Response({"on": "I need to relax.", "off": "Back to work."})


@api_view(['GET'])
def test(request):
    return Response({"text": "Test text: saga :)"})
