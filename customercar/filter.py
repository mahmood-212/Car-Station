from django import forms
import django_filters
from .models import CustomerCar,CarPart
from employee.models import Employee
def get_employee(request):
    return Employee.objects.filter(user=request.user)
class CustomerCar_Filter(django_filters.FilterSet):
    owner_car_name = django_filters.CharFilter(lookup_expr='icontains',label='مالك السيارة')
    employee = django_filters.ModelChoiceFilter(queryset=get_employee)
    date_entery = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = CustomerCar
        fields = ['employee', 'branch', 'owner_car_name', 'owner_car_phone', 'car_company','owner_identity','car_plate','car_color','date_entery','car_under_process','car_ready']

# class CarPart_Filter(django_filters.FilterSet):
#     part_name = django_filters.CharFilter(lookup_expr='icontains')
#     class Meta:
#         model = CarPart
#         fields = ['customer_car', 'part_name', 'part_price','part_invoice']