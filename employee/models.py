from django.db import models
from company.models import CompanyBranch

# Create your models here.
class Employee(models.Model):
    branch_name = models.ForeignKey(CompanyBranch, related_name='companybranch', on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=255, blank=True, null=True)
    employee_phone = models.IntegerField(blank=True, null=True)
    employee_identity = models.IntegerField(blank=True, null=True)
    employee_email = models.EmailField(blank=True, null=True)
    employee_salary = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee_name}"

    