from django.urls import path
<<<<<<< HEAD
from .views import new_Company,new_CompanyBranch, company_details, CompanyBranch_detail, company_update, company_delete,delete_CompanyBranch

=======
from .views import  CompanyBranchs,new_Company,new_CompanyBranch, company_details,delete_CompanyBranch,CompanyBranch_detail,edit_CompanyBranch
# CompanyBranch_detail
>>>>>>> 21e7cad2571c5ad3da3eb798e23ad11ebc9f1537
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