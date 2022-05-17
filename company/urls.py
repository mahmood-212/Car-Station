from django.urls import path
from .views import new_Company,new_CompanyBranch
app_name='accounts'
urlpatterns = [
    path('add_company/', new_Company, name="new_Company"),
    path('add_CompanyBranch/', new_CompanyBranch, name="new_CompanyBranch"),
]