from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CustomerCar_Form,CarPart_Form
from .models import CustomerCar,CarPart
from django.urls import reverse
from django.core.paginator import Paginator
from employee.models import Employee
from company.models import CompanyBranch
from .filter import CustomerCar_Filter

# Create your views here.

@login_required
def CustomerCar_list(request):
    customer_car = CustomerCar.objects.filter(user=request.user).order_by('-date')
    customer_car_filter = CustomerCar_Filter(request.GET, queryset=customer_car,request=request)
    paginator = Paginator(customer_car_filter.qs, 25)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    return render(request,'CustomerCar_list.html',{'customer_car':page_pbj,'count':customer_car.count(),'filter':customer_car_filter})

@login_required
def new_customercar(request):
    if request.method=='POST':
        form = CustomerCar_Form(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            return redirect(reverse('customer:customercar_list'))

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
            # return redirect(reverse('customer:customercar_list'))

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
            return redirect(reverse('customer:customercar_list'))

    else:
        form = CustomerCar_Form(instance=customer_car)
        form.fields['branch'].queryset = CompanyBranch.objects.filter(user=request.user)
        form.fields['employee'].queryset = Employee.objects.filter(user=request.user)
    return render(request, 'update/edit_customercar.html',{'form':form})

@login_required
def edit_carpart(request,id):
    car_part = CarPart.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = CarPart_Form(request.POST, request.FILES,instance=car_part)
        if form.is_valid():
            part = form.save(commit=False)
            part.user = request.user
            part.save()
            # return redirect(reverse(''))

    else:
        form = CarPart_Form(instance=car_part)
        form.fields['customer_car'].queryset = CustomerCar.objects.filter(user=request.user)
    return render(request, 'update/carpart.html',{'form':form})
@login_required
def delete_CustomerCar(request, id):
    customer_car = CustomerCar.objects.get(id=id, user=request.user)
    customer_car.delete()
    return redirect('customer:customercar_list')