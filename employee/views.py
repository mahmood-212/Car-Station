from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from company.models import Company, CompanyBranch
from .forms import Employee_Form
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

'''
    All functions for Employess models
'''

# Add Employee 
@login_required
def add_employee(request):
    if request.method == "POST":
        form= Employee_Form(request.POST)
        if form.is_valid():
            emplyee = form.save(commit=False)
            emplyee.user = request.user
            emplyee.save()
            return redirect(reverse('company:company_details'))
    else:
        form = Employee_Form()
        form.fields['branch_name'].queryset = CompanyBranch.objects.filter(user=request.user)
    return render(request, 'add_employee.html', {'form':form})

# Show details of employee 
@login_required
def employee_details(request):
    employees = Employee.objects.filter(user=request.user)
    return render(request, 'employee_details.html', {'employees':employees})


@login_required
def employee_update(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        
        form = Employee_Form(request.POST, instance=employee)
        if form.is_valid():
            employee1= form.save(commit=False)
            employee1.user = request.user
            employee1.save()
        return redirect('employee:employee_details')
    else:
        form = Employee_Form(instance=employee)
    return render(request, 'employee_update.html', {'form':form})


@login_required
def remove_employee(request, id):
    employee  = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect("employee:emplyee_details")

