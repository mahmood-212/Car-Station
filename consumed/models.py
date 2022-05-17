from django.db import models
from company.models import CompanyBranch
from employee.models import Employee
from invoice.models import Invoice
from accounts.models import User

# Create your models here.

class RequiremtsBranch(models.Model):
    user = models.ForeignKey(User,verbose_name=("المستخدم"), on_delete=models.CASCADE)
    branch = models.ForeignKey(CompanyBranch, related_name='branch', verbose_name="اسم الفرع", on_delete=models.CASCADE)
    employee= models.ForeignKey(Employee, related_name='employee', verbose_name="اسم الموظف",  on_delete=models.CASCADE)
    things_need_name = models.CharField(max_length=255, verbose_name="وصف الطلب", blank=True, null=True)
    things_need_price = models.FloatField(blank=True, verbose_name="سعر الطلب", null=True)


    class Meta():
        verbose_name = 'احتياجات الفرع'
        verbose_name_plural = 'احتياجات الفروع'

    def __str__(self):
        return f"{self.employee.employee_name} - {self.things_need_name}"

class OutCome(models.Model):
    user = models.ForeignKey(User,verbose_name=("المستخدم"), on_delete=models.CASCADE)
    employee_outcome= models.ForeignKey(Employee, related_name='employees', on_delete=models.CASCADE)
    requiremtsbranch = models.ForeignKey(RequiremtsBranch, related_name='requiremtsbranches', on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'مصاريف الفرع'
        verbose_name_plural = 'مصاريف الفروع'

    def __str__(self):
        return f"{self.requiremtsbranch}"

class InCome(models.Model):
    user = models.ForeignKey(User,verbose_name=("المستخدم"), on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, related_name='invoices', on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'دخل الفرع'
        verbose_name_plural = 'دخل الفروع'

    def __str__(self):
        return f"{self.invoice}"
