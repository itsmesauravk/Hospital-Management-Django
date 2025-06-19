from rest_framework import serializers
from .models import Doctor
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import exceptions

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            'id',
            'name',
            'email',
            'password',
            'phone',
            'address',
            'specialist',
            'image',
            'hospital',
            'status'
        ]
        extra_kwargs = {'password': {'write_only': True}}

class DoctorLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            'email',
            'password'
        ]

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                raise exceptions.AuthenticationFailed('No active account found with the given credentials')

        else:
            raise exceptions.ValidationError('Must include "email" and "password"')

        refresh = self.get_token(user)

        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        serializer = DoctorLoginSerializer(user).data
        for k, v in serializer.items():
            data[k] = v

        return data
