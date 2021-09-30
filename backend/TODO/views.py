from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from .serializers import ProjectSerializer, TODOSerializer
from .models import Project, TODO
from rest_framework.viewsets import ModelViewSet
from .filters import ProjectFilter


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class TODOLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
    pagination_class = TODOLimitOffsetPagination

    def destroy(self, request, *args, **kwargs):
        article = get_object_or_404(TODO, pk=kwargs['pk'])
        article.is_active = False
        serializer = TODOSerializer(article)
        return Response(serializer.data)
