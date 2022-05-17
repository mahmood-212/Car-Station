from django.db import models
from company.models import CompanyBranch
from employee.models import Employee
from customercar.models import CustomerCar, CarPart
from accounts.models import User
# Create your models here.

class Invoice(models.Model):
    user = models.ForeignKey(User,verbose_name=("المستخدم"), on_delete=models.CASCADE)
    branch = models.ForeignKey(CompanyBranch, related_name='branchs',verbose_name="اسم الفرع", on_delete=models.CASCADE)
    customercar = models.ForeignKey(CustomerCar, related_name='customercars',verbose_name="اسم مالك السيارة", on_delete=models.CASCADE)
    carpart = models.ForeignKey(CarPart, related_name='carparts', verbose_name="قطع غيار السيارة", on_delete=models.CASCADE)
    work_hand_price = models.FloatField(verbose_name="سعر صيانة", blank=True, null=True)
    tax_price = models.FloatField(verbose_name="الضريبة", blank=True, null=True)
    total_cost = models.FloatField(verbose_name="مبلغ الاجمالي قبل الضريبة", blank=True, null=True)
    total_after_tax = models.FloatField(verbose_name="مبلغ الاجمالي بعد الضريبة", blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name = 'الفاتورة'
        verbose_name_plural = 'الفواتير'
    def __str__(self):
        return self.total_cost


 