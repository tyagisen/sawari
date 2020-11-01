from django.db import models


class Driver(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, unique=True)
    vehicle_type = models.CharField(max_length=100)

