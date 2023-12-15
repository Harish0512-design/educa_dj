from rest_framework.serializers import ModelSerializer

from courses.models import Subject


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ('title',)
