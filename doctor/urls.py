from django.urls import path
from .views import create_doctor,get_doctors,login_doctor

urlpatterns = [
    path('doctors/', get_doctors, name='get-doctors'),
    path('create-doctor/', create_doctor, name='create-doctor'),
    path('login/', login_doctor, name='login-doctor')
]