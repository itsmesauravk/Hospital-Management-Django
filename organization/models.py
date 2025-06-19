from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField()
    logo = models.ImageField(upload_to='company_logo/', blank=True, null=True)


    def __str__(self):
        return f"{self.name}"
    


class Department(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField()


    def __str__(self):
        return f"{self.name}"
    


    
