from rest_framework.serializers import ModelSerializer
# from .models import CustomUser
from .models import Project, TODO


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class TODOSerializer(ModelSerializer):
    project = ProjectSerializer()

    class Meta:
        model = TODO
        fields = '__all__'
