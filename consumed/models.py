from django.db import models
from company.models import CompanyBranch
from employee.models import Employee
from invoice.models import Invoice

# Create your models here.

class RequiremtsBranch(models.Model):
    branch = models.ForeignKey(CompanyBranch, related_name='branchs', on_delete=models.CASCADE)
    employee= models.ForeignKey(Employee, related_name='employees', on_delete=models.CASCADE)
    things_need_name = models.CharField(max_length=255, blank=True, null=True)
    things_need_price = models.FloatField(blank=True, null=True)


class OutCome(models.Model):
    employee= models.ForeignKey(Employee, related_name='employees', on_delete=models.CASCADE)
    requiremtsbranch = models.ForeignKey(Employee, related_name='requiremtsbranchs', on_delete=models.CASCADE)


class InCome(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='invoices', on_delete=models.CASCADE)