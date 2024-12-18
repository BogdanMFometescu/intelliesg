from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    PROFILE_ROLE_CHOICES = [('Data Admin','Data Admin'),
                            ('Data Entry','Data Entry')]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, blank=False, null=False)
    role = models.CharField(max_length=250,blank=False,null=False,choices=PROFILE_ROLE_CHOICES)
    bio = models.CharField(max_length=500,blank=False,null=False)
    phone_number = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    job_title = models.CharField(max_length=250, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)

    def __str__(self):
        return f'{self.user}'
