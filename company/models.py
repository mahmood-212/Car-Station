from django.db import models
# from accounts.models import User
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    user = models.ForeignKey(User,verbose_name=("المستخدم"), on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200,verbose_name="اسم الشركة", blank=True, null=True)
    company_phone = models.IntegerField(blank=True, verbose_name="رقم هاتف الشركة", null=True)
    company_city = models.CharField(max_length=200, verbose_name="المدينة", blank=True, null=True)
    company_address =models.URLField(blank=True, verbose_name="عنوان الشركة", null=True)
    company_code = models.CharField(max_length=255, verbose_name="رقم الفرع", blank=True, null=True)
    company_logo = models.ImageField(blank=True, verbose_name="شعار الشركة", null=True)

    class Meta():
        verbose_name = 'الشركة'
        verbose_name_plural = 'الشركات'

    def __str__(self):
        return self.company_name

class CompanyBranch(models.Model):
    user = models.ForeignKey(User,verbose_name=("المستخدم"), on_delete=models.CASCADE)
    company_name = models.ForeignKey(Company, related_name='company', verbose_name="اسم الشركة ", on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=255, verbose_name="اسم الفرع", blank=True, null=True)
    branch_phone = models.IntegerField(verbose_name="رقم هاتف الفرع", blank=True, null=True)
    branch_code = models.CharField(max_length=255,verbose_name="رقم الفرع", blank=True, null=True)
    branch_city = models.CharField(max_length=255,verbose_name="المدينة", blank=True, null=True)
    branch_address = models.URLField(verbose_name="عنوان الفرع", blank=True, null=True)

    class Meta():
        verbose_name = 'الفرع'
        verbose_name_plural = 'الفروع'

    def __str__(self):
        return self.branch_name




