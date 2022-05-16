import django_filters
from .models import RequiremtsBranch

class RequiremtsBranch_Filter(django_filters.FilterSet):
    things_need_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = RequiremtsBranch
        fields = ['branch', 'employee', 'things_need_name', 'things_need_price']