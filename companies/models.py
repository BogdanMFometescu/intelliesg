from django.db import models
from common.models import BaseIdentifierClass
from users.models import Profile

class Company(BaseIdentifierClass):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(unique=True, blank=False, null=False,max_length=255)
    address = models.CharField(max_length=255, blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False)
    country = models.CharField(max_length=255, blank=False, null=False)
    phone = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    logo = models.ImageField(upload_to='company_logos',blank=True, null=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f'{self.name}'
    
