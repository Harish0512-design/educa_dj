from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from courses.models import Subject
from courses.serializer import SubjectSerializer


# Create your views here.
class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
