from django.urls import path
from .views import CarPart_list, CustomerCar_details,CarPart_details ,new_customercar,new_carpart,edit_customercar,edit_carpart,CustomerCar_list,delete_CustomerCar,delete_CarPart
app_name='customercar'
urlpatterns = [
    path('add_customer_car/', new_customercar, name="new_customercar"),
    path('edit_customer_car/<int:id>/', edit_customercar, name="edit_customercar"),
    path('add_car_part/', new_carpart, name="new_carpart"),
    path('edit_car_part/<int:id>/', edit_carpart, name="edit_carpart"),
    path('customercar_list/',CustomerCar_list,name='customercar_list'),
    path('CustomerCar_details/<int:id>/',CustomerCar_details,name='CustomerCar_details'),
    path('CarPart_details/<int:id>/',CarPart_details,name='CarPart_details'),
    path('carpart_list/',CarPart_list,name='carpart_list'),
    path('delete_customer_car/<int:id>/',delete_CustomerCar,name='delete_CustomerCar'),
    path('delete_car_part/<int:id>/',delete_CarPart,name='delete_CarPart'),
]