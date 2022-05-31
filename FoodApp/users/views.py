import re
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST': #if signup hit
        form = RegisterForm(request.POST) #check data
        if form.is_valid(): #info is valid or not
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'welcome {username} to food page')
            return redirect('login')
    else: #new user
        form = RegisterForm()
    return render(request, 'users/reg.html', {'form':form}) #new user directed to this reg page

@login_required
def profile(request):
    return render(request, 'users/profile.html')