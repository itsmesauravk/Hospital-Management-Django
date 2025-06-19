from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Patient
from .serilizers import PatientSerializer

from django.http import HttpResponse

# Create your views here.  >> This is the place where we write the logic of our application

@api_view(['POST'])
def create_patient(request):
    print(request.data)
    serilizer = PatientSerializer(request.data)
    print(serilizer.data)
    patient = Patient.objects.create(serilizer.data)
    if serilizer.is_valid():
        patient.save()
        return Response({'message': 'Patient created successfully'}, serilizer.data, status=201)
    else:
        return Response(serilizer.errors, status=400)





