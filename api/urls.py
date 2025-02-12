from django.urls import path
from .views import (
    home, view_records, add_employee, edit_employee, delete_employee,
    EmployeeListCreate, EmployeeDetail
)

urlpatterns = [
    path('', home, name='home'),
    path('view-records/', view_records, name='view_records'),
    path('add-employee/', add_employee, name='add_employee'),
    path('edit-employee/<int:pk>/', edit_employee, name='edit_employee'),
    path('delete-employee/<int:pk>/', delete_employee, name='delete_employee'),

    # API URLs
    path('api/employees/', EmployeeListCreate.as_view(), name='employee-list'),
    path('api/employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
]
