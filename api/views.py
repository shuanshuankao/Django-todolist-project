from django.shortcuts import render
from .serializers import TodoSerializers
from rest_framework import viewsets
from todo.models import Todo

# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializers

    def get_queryset(self):
        return Todo.objects.all().order_by("-created")
