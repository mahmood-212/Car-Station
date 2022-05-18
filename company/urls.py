from django.urls import path
from .views import  CompanyBranchs,new_Company,new_CompanyBranch, company_details,delete_CompanyBranch,CompanyBranch_detail
# CompanyBranch_detail
app_name='accounts'
urlpatterns = [
    path('add_company/', new_Company, name="new_Company"),
    path('company_branchs/', CompanyBranchs, name="CompanyBranchs"),
    path('companybranch_detail/<int:id>', CompanyBranch_detail, name="CompanyBranch_detail"),
    path('<int:id>/add_CompanyBranch/', new_CompanyBranch, name="new_CompanyBranch"),
    path('delete_companybranch/<int:id>/', delete_CompanyBranch, name="delete_CompanyBranch"),
    path('company_details/', company_details, name='company_details'),
]