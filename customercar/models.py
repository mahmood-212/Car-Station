from django.db import models
from employee.models import Employee
from company.models import CompanyBranch
# Create your models here.

class CustomerCar(models.Model):
    employee = models.ForeignKey(Employee, related_name='emplyees', on_delete=models.CASCADE)
    branch = models.ForeignKey(CompanyBranch, related_name='branches', on_delete=models.CASCADE)
    owner_car_name = models.CharField(max_length=255, blank=True, null=True)
    owner_car_phone = models.IntegerField(blank=True, null=True)
    car_company = models.CharField(max_length=255, blank=True, null=True)
    owner_identity = models.IntegerField(blank=True, null=True)
    car_plate = models.CharField(max_length=255, blank=True, null=True)
    car_color = models.CharField(max_length=255, blank=True, null=True)
    date_entery = models.DateTimeField(auto_now=True)
    car_under_process = models.BooleanField(default=True, blank=True, null=True)
    car_ready = models.BooleanField(default=False, blank=True, null=True)

    def  __str__(self):
        return f"{self.owner_car_name} - {self.car_plate}"



class CarPart(models.Model):
    customer_car = models.ForeignKey(CustomerCar, related_name='customercar', on_delete=models.CASCADE)
    part_name = models.CharField(max_length=255, blank=True, null=True)
    part_price = models.IntegerField(blank=True, null=True)
    part_invoice = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.part_name}"




