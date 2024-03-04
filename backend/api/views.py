from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer