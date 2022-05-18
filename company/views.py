from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import Company_Form,CompanyBranch_Form
from .models import Company,CompanyBranch
from django.urls import reverse
# Create your views here.
@login_required
def CompanyBranchs(request):
    companybranch = CompanyBranch.objects.filter(user=request.user)
    return render(request,'CompanyBranchs.html', {'branch':companybranch})
@login_required
def new_Company(request):
    if request.method=='POST':
        form = Company_Form(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.save()
            # return redirect(reverse(''))

    else:
        form = Company_Form()
    return render(request, 'new/Company_Form.html',{'form':form})
@login_required
def CompanyBranch_detail(request, id):
    CompanyBranch_detail = CompanyBranch.objects.filter(id=id, user=request.user)
    return render(request, 'CompanyBranch_detail.html', context={'CompanyBranch':CompanyBranch_detail})
@login_required
def new_CompanyBranch(request):
    if request.method=='POST':
        form = CompanyBranch_Form(request.POST)
        if form.is_valid():
            CompBranch = form.save(commit=False)
            CompBranch.user = request.user
            CompBranch.save()
            # return redirect(reverse(''))

    else:
        form = CompanyBranch_Form()
        form.fields['company_name'].queryset = Company.objects.filter(user=request.user)
    return render(request, 'new/CompanyBranch_Form.html',{'form':form})

@login_required
def company_details(request):
    company = Company.objects.all()

    return render(request, 'company_details.html', {'company':company})


@login_required
def delete_CompanyBranch(request, id):
    branch = CompanyBranch.objects.get(id=id, user=request.user)
    branch.delete()
    return redirect('company:CompanyBranchs')