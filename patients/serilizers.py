from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'id',
            'name',
            'age',
            'problem',
            'date',
            'time',
            'contact',
            'company',
            'department',
        ]
        