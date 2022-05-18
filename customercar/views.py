from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CustomerCar_Form,CarPart_Form
from .models import CustomerCar,CarPart
from django.urls import reverse
from django.core.paginator import Paginator
from employee.models import Employee
from company.models import CompanyBranch
# Create your views here.

@login_required
def new_customercar(request):
    if request.method=='POST':
        form = CustomerCar_Form(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            # return redirect(reverse(''))

    else:
        form = CustomerCar_Form()
        form.fields['branch'].queryset = CompanyBranch.objects.filter(user=request.user)
        form.fields['employee'].queryset = Employee.objects.filter(user=request.user)
    return render(request, 'new/customercar.html',{'form':form})

@login_required
def new_carpart(request):
    if request.method=='POST':
        form = CarPart_Form(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            # return redirect(reverse(''))

    else:
        form = CarPart_Form()
        form.fields['customer_car'].queryset = CustomerCar.objects.filter(user=request.user)
    return render(request, 'new/carpart.html',{'form':form})

@login_required
def edit_customercar(request, id):
    customer_car = CustomerCar.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = CustomerCar_Form(request.POST,instance=customer_car)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            # return redirect(reverse('company:branches'))

    else:
        form = CustomerCar_Form(instance=customer_car)
        form.fields['branch'].queryset = CompanyBranch.objects.filter(user=request.user)
        form.fields['employee'].queryset = Employee.objects.filter(user=request.user)
    return render(request, 'update/edit_customercar.html',{'form':form})