from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm
from . import forms
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
         form = forms.UserRegisterForm(request.POST)
         if form.is_valid():
             user = form.save()
             login(request, user)
             return redirect('Accounts:register')
    else:
    	form = forms.UserRegisterForm()
    return render(request, 'Accounts/signup.html', { 'form': form })

@login_required(login_url="/Accounts/login/")
def register_view(request):
    if request.method == "POST":
        form = forms.CreateProfile(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.Username = request.user
            instance.Email_Address = request.user.email 
            instance.save()
            return redirect('Accounts:login')
    else:
        form = forms.CreateProfile()
    return render(request, 'Accounts/register.html', { 'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else: 
                return redirect('Accounts:profile')
    else:
    	form = AuthenticationForm()
    return render(request, 'Accounts/login.html', { 'form': form })

@login_required(login_url="/Accounts/login/")
def profile_view(request):
    return render(request, 'Accounts/profile.html')

@login_required(login_url="/Accounts/login/")
def logout_view(request):
	logout(request)
	return redirect('home')
