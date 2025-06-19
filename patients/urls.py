from .views import create_patient
from django.urls import path



urlpatterns = [
    path('create-patient/', create_patient, name='create-patient'),
]