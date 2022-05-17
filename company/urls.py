from django.urls import path
from .views import new_Company
app_name='accounts'
urlpatterns = [
    path('add_company/', new_Company, name="new_Company"),
]