from django.shortcuts import render,get_object_or_404, redirect
from .models import RequiremtsBranch, OutCome, InCome
from .forms import RequiremtsBranch_Form, OutComeForm
from django.contrib.auth.decorators import login_required
from company.models import CompanyBranch
from employee.models import Employee

# Create your views here.

@login_required
def add_requirement(request):
    # branch_name= get_object_or_404(CompanyBranch, id=request.user.id)
    form = RequiremtsBranch_Form()
    if request.method == 'POST':
        form = RequiremtsBranch_Form(request.POST)
        if form.is_valid():
            requirement_branch = form.save(commit=False)
            requirement_branch.user = request.user
            # requirement_branch.branch = CompanyBranch.objects.get(branch=request.user.branch)

            print(f"from is valid $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            requirement_branch.save()
            return redirect('consumed:branch_requirement')
        
    else:
        print(f"from else of is post")
        form = RequiremtsBranch_Form()
        form.fields["branch"].queryset = CompanyBranch.objects.filter(user=request.user)
        form.fields["employee"].queryset = Employee.objects.filter(user=request.user)
        print(f"after filter form")
    return render(request, 'add_requirements.html', {'form':form})

