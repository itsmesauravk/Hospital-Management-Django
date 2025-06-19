from django.db import models
from organization.models import Company,Department

#creating model (Patient)

class Patient(models.Model):
    # id will be set autometically with primary key and auto increment
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=3)
    problem = models.TextField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    contact = models.IntegerField(max_length=10)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)   
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return f"{self.name}"
    
