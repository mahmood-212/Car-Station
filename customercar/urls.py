from django.urls import path
from .views import new_customercar,new_carpart
app_name='customercar'
urlpatterns = [
    path('add_customer_car/', new_customercar, name="new_customercar"),
    path('add_car_part/', new_carpart, name="new_carpart"),
]