from django.db import models
from company.models import CompanyBranch
# from accounts.models import User
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    user = models.ForeignKey(User,verbose_name=("المستخدم"), on_delete=models.CASCADE)
    branch_name = models.ForeignKey(CompanyBranch, related_name='companybranches', verbose_name="اسم الفرع", on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=255, verbose_name="اسم الموظف", blank=True, null=True)
    employee_phone = models.IntegerField(verbose_name="هاتف الموظف", blank=True, null=True)
    employee_identity = models.IntegerField(verbose_name="رقم هوية الموظف", blank=True, null=True)
    employee_email = models.EmailField(verbose_name="ايميل الموظف", blank=True, null=True)
    employee_salary = models.FloatField(verbose_name="راتب الموظف", blank=True, null=True)


    class Meta():
        verbose_name = 'الموظف'
        verbose_name_plural = 'الموظفين'

    def __str__(self):
        return f"{self.employee_name}"

    