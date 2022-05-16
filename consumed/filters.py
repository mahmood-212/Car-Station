import django_filters
from .models import RequiremtsBranch,InCome,OutCome

# class RequiremtsBranch_Filter(django_filters.FilterSet):
#     name = django_filters.CharFilter(lookup_expr='icontains')
#     class Meta:
#         model = RequiremtsBranch
#         fields = ['name', 'age', 'boy_class', 'number_kawme', 'number_phone']