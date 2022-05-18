from django.urls import path
from .views import new_Company,new_CompanyBranch, company_details, CompanyBranch_detail, company_update, company_delete,delete_CompanyBranch,edit_CompanyBranch

app_name='accounts'
urlpatterns = [
    path('add_company/', new_Company, name="new_Company"),
    path('companybranch_detail/<int:id>', CompanyBranch_detail, name="CompanyBranch_detail"),
    path('edit_branch/<int:id>', edit_CompanyBranch, name="edit_branch"),
    path('<int:id>/add_CompanyBranch/', new_CompanyBranch, name="new_CompanyBranch"),
    path('delete_companybranch/<int:id>/', delete_CompanyBranch, name="delete_CompanyBranch"),
    path('company_details/', company_details, name='company_details'),
    path('<int:id>/company_update/', company_update, name='company_update'),
    path('<int:id>/company_delete/', company_delete, name='company_delete')
]
