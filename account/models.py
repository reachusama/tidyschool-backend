from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)
    is_ai = models.BooleanField('ai status', default=False)
    address = models.CharField(max_length=300, default='', null=True, blank=True)
    first_name = models.CharField(max_length=300, default='', null=True, blank=True)
    last_name = models.CharField(max_length=300, default='', null=True, blank=True)
