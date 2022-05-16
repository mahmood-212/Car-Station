import django_filters
from .models import Employee

class CarPart_Filter(django_filters.FilterSet):
    employee_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Employee
        fields = ['branch_name', 'employee_phone', 'employee_identity','employee_email','employee_salary']