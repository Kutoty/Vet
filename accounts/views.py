from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from . forms import RegistrationForm, AccountAuthenticationForm, VetRegistrationForm
from  . models import Specialization
from .county import counties


def registration_view(request):
    context = {}
    context['counties'] = counties
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            account = form.save()
            if account.role == "vet":
                data = {}
                data['account'] = account.id
                data['specialization'] = request.POST.get('specialization')
                data['vetNo'] = request.POST.get('vetNo')
                form = VetRegistrationForm(data)
                if form.is_valid():
                    form.save()
                    return redirect('login_view')
                else:
                    print(form.errors)
            else:
                return redirect('login_view')
        else:
            print(form.errors)
            # form.save()
            # return redirect('login_view')
    return render(request, 'accounts/register.html',context)



def create_vet_account(request):
    context = {}    
    specialization = Specialization.objects.all()
    context['specialization'] = specialization
    context['counties'] = counties
    return render(request, 'accounts/vetRegister.html',context)


def login_view(request):
    context = {}
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                if user.is_admin:
                    return redirect('admin_home_dashboard')
                elif user.role == "vet":
                    return redirect('vet_home_view')
                else:
                    return redirect('farmer_home_view')
    return render(request, 'accounts/login.html')


@login_required(login_url='login_view')
def logout_view(request):
    logout(request)

    return redirect('login_view')
