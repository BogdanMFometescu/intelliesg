from django.db import models
import uuid

class BaseIdentifierClass(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    id = models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4,editable=False)

    class Meta:
        abstract = True
