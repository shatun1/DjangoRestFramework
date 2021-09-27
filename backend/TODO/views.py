from django.shortcuts import render
from .serializers import ProjectSerializer, TODOSerializer
from .models import Project, TODO
from rest_framework.viewsets import ModelViewSet


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer