from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    user = models.ForeignKey(User,verbose_name=("المستخدم"), on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    company_phone = models.IntegerField(blank=True, null=True)
    company_city = models.CharField(max_length=200, blank=True, null=True)
    company_address =models.CharField(max_length=200,blank=True, null=True)
    company_code = models.CharField(max_length=255, blank=True, null=True)
    company_logo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.company_name

class CompanyBranch(models.Model):
    user = models.ForeignKey(User,verbose_name=("المستخدم"), on_delete=models.CASCADE)
    company_name = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=255, blank=True, null=True)
    branch_phone = models.IntegerField(blank=True, null=True)
    branch_code = models.CharField(max_length=255, blank=True, null=True)
    branch_city = models.CharField(max_length=255, blank=True, null=True)
    branch_address = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.branch_name




