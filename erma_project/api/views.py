from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ProjectViewSet(ModelViewSet):

    model = Project
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
