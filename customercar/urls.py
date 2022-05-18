from django.urls import path
from .views import new_customercar
app_name='customercar'
urlpatterns = [
    path('add_customer_car/', new_customercar, name="v"),
]