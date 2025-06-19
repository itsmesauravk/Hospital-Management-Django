from django.db import models
from organization.models import Company

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    specialist = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctors', blank=True, null=True)
    hospital = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name