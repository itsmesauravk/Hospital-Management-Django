from django.contrib import admin


# Import your models here.
from .models import Company, Department

#for registering the model in the admin panel
admin.site.register([Company, Department])
