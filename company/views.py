from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import Company_Form,CompanyBranch_Form
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
