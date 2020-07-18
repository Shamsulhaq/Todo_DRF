from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ListSerializer
from .models import List


# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all().order_by('keyword')
    serializer_class = ListSerializer
