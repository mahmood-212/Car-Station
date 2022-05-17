from django.db import models
from company.models import CompanyBranch
from employee.models import Employee
from customercar.models import CustomerCar, CarPart
from django.contrib.auth.models import User
# Create your models here.

class Invoice(models.Model):
    user = models.ForeignKey(User,verbose_name=("المستخدم"), on_delete=models.CASCADE)
    branch = models.ForeignKey(CompanyBranch, related_name='branchs', on_delete=models.CASCADE)
    customercar = models.ForeignKey(CustomerCar, related_name='customercars', on_delete=models.CASCADE)
    carpart = models.ForeignKey(CarPart, related_name='carparts', on_delete=models.CASCADE)
    work_hand_price = models.FloatField(blank=True, null=True)
    tax_price = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    total_after_tax = models.FloatField(blank=True, null=True)
    # created_date = models.DateTimeField(auto_now=True)


 