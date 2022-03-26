from django.contrib.auth.models import AbstractUser
from djongo import models
from django.conf import settings


class User(AbstractUser):
    """
        This is the base user model, a User can have multiple access, such as Teacher & AI
    """
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)
    is_ai = models.BooleanField('ai status', default=False)


class Teacher(models.Model):
    """
        Teacher Mode: Add new params as required
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=300, null=True, blank=True, default='')
    first_name = models.CharField(max_length=300, null=True, blank=True, default='')
    last_name = models.CharField(max_length=300, null=True, blank=True, default='')


class Student(models.Model):
    """
        Student Mode: Add new params as required
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=300, null=True, blank=True, default='')
    first_name = models.CharField(max_length=300, null=True, blank=True, default='')
    last_name = models.CharField(max_length=300, null=True, blank=True, default='')


class AI(models.Model):
    """
        AI Mode: Add new params as required
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=300, null=True, blank=True, default='')
    first_name = models.CharField(max_length=300, null=True, blank=True, default='')
    last_name = models.CharField(max_length=300, null=True, blank=True, default='')
