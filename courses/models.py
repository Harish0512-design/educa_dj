from django.contrib.auth.models import User
from django.db import models

from commons.models import BaseModel


# Create your models here.
class Subject(BaseModel):
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Course(BaseModel):
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE, related_name='courses')
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='courses_created')
    overview = models.TextField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Module(BaseModel):
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, related_name='modules')
    description = models.TextField()

    def __str__(self):
        return self.title
