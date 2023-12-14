from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BaseModel(models.Model):
    title = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ItemBaseModel(BaseModel):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='%(class)s_related')

    class Meta:
        abstract = True
