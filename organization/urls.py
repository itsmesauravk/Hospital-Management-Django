from django.urls import path
from .views import company_list,company_detail ,company_create, company_update, company_delete, view_department, create_department, login

urlpatterns = [
    path('companies/', company_list, name='company-list'), # (url, function, uniqueName)
    path('create-company/', company_create, name='company-create' ),
    path('update-company/<int:pk>',company_update, name='company-update'),
    path('delete-company/<int:pk>', company_delete, name='company-delete'),
    path('company-detail/<int:pk>', company_detail, name='company-detail')
]

departmentpatterns = [
    path('departments/',view_department, name='view-departent'),
    path('create-department/',create_department, name='create-department')
]

userlogin = [
    path('login/', login, name='login')
]

urlpatterns += departmentpatterns
urlpatterns += userlogin