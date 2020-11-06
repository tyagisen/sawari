from django.db import models
from .validators import validate_number
from django.core import validators


class Driver(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, unique=True, validators=[validate_number])
    vehicle_type = models.CharField(max_length=100)

# alidators.MinLengthValidator(10)