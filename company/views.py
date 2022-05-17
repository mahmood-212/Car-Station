from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import Company_Form,CompanyBranch_Form
from .models import Company,CompanyBranch
from django.urls import reverse
# Create your views here.
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
