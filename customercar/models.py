from datetime import datetime
from django.db import models
from employee.models import Employee
from company.models import CompanyBranch
from django.contrib.auth.models import User
# Create your models here.

class CustomerCar(models.Model):
    user = models.ForeignKey(User,verbose_name=("المستخدم"), on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name='emplyees', verbose_name="اسم الموظف", on_delete=models.CASCADE, blank=True, null=True)
    branch = models.ForeignKey(CompanyBranch, related_name='branches', verbose_name="اسم الفرع", on_delete=models.CASCADE, blank=True, null=True)
    owner_car_name = models.CharField(max_length=255, verbose_name="اسم مالك السيارة")
    owner_car_phone = models.IntegerField(verbose_name="رقم هاتف المالك", blank=True, null=True)
    car_company = models.CharField(max_length=255, verbose_name="ماركت السيارة",  blank=True, null=True)
    owner_identity = models.IntegerField(blank=True, verbose_name="رقم هوية المالك", null=True)
    car_plate = models.CharField(max_length=255, verbose_name="رقم اللوحة", blank=True, null=True)
    car_color = models.CharField(max_length=255, verbose_name="لون السيارة", blank=True, null=True)
    date_entery = models.DateTimeField(auto_now=True, verbose_name="تاريخ استلام المركبة")
    car_under_process = models.BooleanField(default=True, verbose_name="السيارة في الصيانة")
    car_ready = models.BooleanField(default=False, verbose_name="السيارة جاهزه للاستلام")
    date = models.DateTimeField(auto_now=True,blank=True,null=True)

    class Meta():
        verbose_name = 'سيارة العميل'
        verbose_name_plural = 'سيارات العملاء'
    def  __str__(self):
        return f"{self.owner_car_name} - {self.car_plate}"

    def save(self, *args, **kwargs):
        if self.date == None:
            self.date = datetime.now()
        super().save(*args, **kwargs)


class CarPart(models.Model):
    user = models.ForeignKey(User,verbose_name=("المستخدم"), on_delete=models.CASCADE)
    customer_car = models.ForeignKey(CustomerCar, related_name='customercar', verbose_name=" رقم السيارة العميل", on_delete=models.CASCADE)
    part_name = models.CharField(max_length=255,  verbose_name=" اسم القطعة الغيار")
    part_price = models.IntegerField(verbose_name=" سعر قطعة الغيار")
    part_invoice = models.ImageField(verbose_name=" ارفاق صورة الفواتير قطع الغيار", blank=True, null=True)
    date = models.DateField(auto_now=True,blank=True,null=True)
    class Meta():
        verbose_name = 'قطع غيار السيارة'
        verbose_name_plural = 'قطع غيار السيارات'


    def __str__(self):
        return f"{self.part_name}"




