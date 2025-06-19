from django.shortcuts import render
from .models import Company, Department
from .serializers import CompanySerializer, DepartmentSerializer, MyTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes #for api view
from rest_framework.permissions import IsAuthenticated #for authentication
from rest_framework import status

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def company_list(request):
    company = Company.objects.all()
    serializer = CompanySerializer(company, many=True)
    return Response(serializer.data)

# get specific hospital
@api_view(['GET'])
def company_detail(request,pk):
    company = Company.objects.get(pk=pk)
    serializer = CompanySerializer(company, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)
   
    

@api_view(['POST'])
def company_create(request):
    print(request.data)
    serializer = CompanySerializer(data=request.data) 

    if serializer.is_valid():
        serializer.save()
        response = Response(serializer.data, status=status.HTTP_201_CREATED)
        print(response.status_code)
        return response
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['PATCH'])
def company_update(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CompanySerializer(company, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['DELETE'])
def company_delete(request, pk):
    try:
        company = Company.objects.get(pk=pk)
        # serializer = CompanySerializer(company)
    except Company.DoesNotExist:
        return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)

    company.delete()
    return Response("Delete Successful", status=status.HTTP_204_NO_CONTENT)





# FOR DEPARTMENT

@api_view(['GET'])
def view_department(request):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many= True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_department(request):
    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#add department from company id from params


# while viewing the company details, we can see the departments of that company



# For login 
@api_view(['POST'])
def login(request):
    serializer = MyTokenObtainPairSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



