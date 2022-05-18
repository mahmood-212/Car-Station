from django.urls import path
from .views import new_customercar,new_carpart,edit_customercar
app_name='customercar'
urlpatterns = [
    path('add_customer_car/', new_customercar, name="new_customercar"),
    path('edit_customer_car/<int:id>/', edit_customercar, name="edit_customercar"),
    path('add_car_part/', new_carpart, name="new_carpart"),
]