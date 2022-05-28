from django.urls import path
from .views import add_employee, employee_details, employee_update, remove_employee


app_name='employee'
urlpatterns = [
    path('add_employee/', add_employee, name='add_employee'),
    path('employee_details/', employee_details, name='employee_details'),
    path('employee_update/<int:id>/', employee_update, name='update_emplyee'),
    path('remove_employee/<int:id>/', remove_employee, name='remove_employee'),
]