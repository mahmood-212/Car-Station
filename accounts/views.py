from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def sinup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('')
    return render(request, 'sinup.html',{'form':form})