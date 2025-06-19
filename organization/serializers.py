from typing import Any, Dict
from rest_framework import serializers
from .models import Company, Department
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CompanySerializer(serializers.ModelSerializer):
    #class Meta is a behavior of the class
    #fields is a list of fields that we want to serialize or parse
    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'location',
            'phone',
            'email',
            'website'
        ]


class DepartmentSerializer(serializers.ModelSerializer):
    company=CompanySerializer()
    class Meta:
        model = Department
        fields = [
            'id',
            'name',
            'company',
            'location',
            'email',
            'website'
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data=super().validate(attrs)
        serializers = UserSerializer(self.user).data
        for k,v in serializers.items():
            data[k]=v
        return data