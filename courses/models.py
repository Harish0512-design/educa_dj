from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from commons.models import BaseModel, ItemBaseModel


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


class Content(models.Model):
    module = models.ForeignKey(to=Module, on_delete=models.CASCADE, related_name='contents')
    content_type = models.ForeignKey(to=ContentType, on_delete=models.CASCADE,
                                     limit_choices_to={'model__in': ('text', 'image', 'file', 'video')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')


class Text(ItemBaseModel):
    content = models.TextField()


class Image(ItemBaseModel):
    image = models.ImageField(upload_to='images')


class Video(ItemBaseModel):
    video_url = models.URLField()


class File(ItemBaseModel):
    file = models.FileField(upload_to='files')
