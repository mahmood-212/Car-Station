import django_filters
from .models import CustomerCar,CarPart

class CustomerCar_Filter(django_filters.FilterSet):
    owner_car_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = CustomerCar
        fields = ['employee', 'branch', 'owner_car_name', 'owner_car_phone', 'car_company','owner_identity','car_plate','car_color','date_entery','car_under_process','car_ready']

class CarPart_Filter(django_filters.FilterSet):
    part_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = CustomerCar
        fields = ['customer_car', 'part_name', 'part_price','part_invoice']