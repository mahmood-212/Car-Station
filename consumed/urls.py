from django.urls import path
from .views import add_requirement


app_name='consumed'

urlpatterns=[
    path('add_consumed/', add_requirement, name='branch_requirement')
]