import re
from django.shortcuts import render
from .forms import UserForm, GameetUserForm
from django.http import HttpResponseRedirect

# Create your views here.

def register(request):
    submitted = False
    if request.method == "POST":
        form1 = UserForm(request.POST)
        form2 = GameetUserForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            gameetUser = form2.save(commit=False)
            gameetUser.user = form1.save()
            gameetUser.save()
            return HttpResponseRedirect('/register?submitted=True')
    else:
        form1 = UserForm()
        form2 = GameetUserForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'register.html',{'form1': form1, 'form2': form2,'submitted':submitted})