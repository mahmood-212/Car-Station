import django_filters
from .models import Invoice

class Invoice_Filter(django_filters.FilterSet):
    class Meta:
        model = Invoice
        fields = ['branch', 'customercar', 'carpart','work_hand_price','tax_price','total_cost','total_after_tax']