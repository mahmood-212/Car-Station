from django.urls import path
from .views import new_Company,new_CompanyBranch, company_details
# CompanyBranch_detail
app_name='accounts'
urlpatterns = [
    path('add_company/', new_Company, name="new_Company"),
    # path('companybranch_detail/<int:id>', CompanyBranch_detail, name="CompanyBranch_detail"),
    path('<int:id>/add_CompanyBranch/', new_CompanyBranch, name="new_CompanyBranch"),
    path('company_details/', company_details, name='company_details'),
]