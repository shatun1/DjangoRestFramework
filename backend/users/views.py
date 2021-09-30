from rest_framework import mixins, viewsets

from rest_framework.renderers import JSONRenderer


from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializers import UserSerializer


# class UserModelViewSet(ModelViewSet):
#     renderer_classes = [JSONRenderer]
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer


class UserCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                       viewsets.GenericViewSet, viewsets.ViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
