from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import Company_Form,CompanyBranch_Form
from .models import Company,CompanyBranch
from django.urls import reverse
from django.core.paginator import Paginator

# Create your views here.

'''
Home page
'''
@login_required
def home(request):
    company = Company.objects.filter(user=request.user)
    print(f"{company} ########################")
    return render(request,'home.html', {'company':company})


'''
    All functions for Company models
'''

#  Add New Company 
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


# Show all Company Details
@login_required
def company_details(request):
    company = Company.objects.filter(user=request.user)
    branches = CompanyBranch.objects.filter(user=request.user,company_name__in=company)
    return render(request, 'company_details.html', {'company':company,'branches':branches})

# Edit In Company Details 
@login_required
def company_update(request, id):
    company = get_object_or_404(Company, id=id, user=request.user)

    if request.method == "POST":
        form = Company_Form(request.POST, instance=company)
        if form.is_valid():
            company1 = form.save(commit=False)
            company1.user = request.user
            company1.save()
        return redirect('company:company_details', id=company.id)
    else:
        form = Company_Form(instance=company)
    return render(request, 'company_edit.html', {'form':form})


# Company Delete Details
@login_required
def company_delete(request, id):
    company = get_object_or_404(Company, id=id)
    company.delete()
    return redirect('company:new_Company')


'''
   All functions for  CompanyBranch models
'''

# Add New CompanyBranch
@login_required
def new_CompanyBranch(request, company_id):
    company = Company.objects.get(user=request.user, id=company_id)
    if request.method=='POST':
        form = CompanyBranch_Form(request.POST)
        if form.is_valid():
            CompBranch = form.save(commit=False)
            CompBranch.user = request.user
            CompBranch.company_name = company
            CompBranch.save()
            return redirect(reverse('company:branches'))

    else:
        form = CompanyBranch_Form()
        # form.fields['company_name'].queryset = Company.objects.filter(user=request.user)
    return render(request, 'new/CompanyBranch_Form.html',{'form':form})

# Show all CompanyBrache Details
@login_required
def CompanyBranch_detail(request,id):
    CompanyBranch_detail = CompanyBranch.objects.filter(id=id,user=request.user)
    return render(request, 'CompanyBranch_detail.html', context={'CompanyBranch':CompanyBranch_detail})



#  Edit IN CompanyBranch
@login_required
def edit_CompanyBranch(request, id):
    branch = CompanyBranch.objects.get(id=id, user=request.user)
    if request.method=='POST':
        form = CompanyBranch_Form(request.POST, request.FILES, instance=branch)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('company:branches'))

    else:
        form = CompanyBranch_Form(instance=branch)
    return render(request, 'update/edit_CompanyBranch.html',{'form':form})


# Delete CompanyBranch 
@login_required
def delete_CompanyBranch(request, id):
    branch = CompanyBranch.objects.get(id=id, user=request.user)
    branch.delete()
    return redirect('company:branches')



@login_required
def CompanyBranchs(request):
    companybranch = CompanyBranch.objects.filter(user=request.user)
    paginator = Paginator(companybranch,25)
    page_number = request.GET.get('page')
    page_pbj = paginator.get_page(page_number)
    return render(request,'CompanyBranchs.html', {'branch':page_pbj})





        
    

        






