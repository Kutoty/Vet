from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . forms import BreedRegistrationForm, AddAnimalForm,AddSpecializationForm,BookVetForm  
from django.contrib import messages
from . models import AnimalRecord, BookVet, Breed
from accounts.models import Account, Specialization, Vet
from django.core.mail import send_mail
import random


@login_required(login_url='login_view')
def admin_home_dashboard(request):
    context = {}
    vets = Account.objects.filter(role="vet")
    farmers = Account.objects.filter(role="common_user")
    animal_count = AnimalRecord.objects.all().count()
    context['animal_count'] = animal_count
    context['vets'] = vets
    context['farmers'] = farmers
    context['vet_count'] = vets.count()
    context['farmers_count'] = farmers.count()
    return render(request, 'livestock/admin_home_dashboard.html', context)

@login_required(login_url='login_view')
def add_specialization(request):
    if request.POST:
        form = AddSpecializationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_home_dashboard')
        else:
            print(form.errors)
    return redirect('admin_home_dashboard')


@login_required(login_url='login_view')
def vet_home_view(request):
    context = {}
    vet = Vet.objects.get(account=request.user.id)
    clients = BookVet.objects.filter(vet = vet.id)
    print(clients)
    context['clients'] = clients
    return render(request, 'livestock/vet_home_view.html',context)


@login_required(login_url='login_view')
def farmer_home_view(request):
    context = {}
    context['breeds'] = Breed.objects.filter(farmer=request.user)
    context['animals'] = AnimalRecord.objects.filter(farmer=request.user)
    context['specialization'] = Specialization.objects.all()
    return render(request, 'livestock/farmer_home_view.html', context)


@login_required(login_url='login_view')
def add_breed(request):
    if request.POST:
        data = {}
        data['name'] = request.POST.get('name')
        data['farmer'] = request.user
        form = BreedRegistrationForm(data)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO,
                                 'Breed successfully added')
            return redirect("farmer_home_view")
        else:
            messages.add_message(request, messages.ERROR, "invalid form")
    return redirect("farmer_home_view")


def add_animal(request):
    if request.POST:
        data = request.POST
        data._mutable = True
        data['farmer'] = request.user

        # data['age'] = datetime.date.today().year - request.POST.get('birth_date')
        form = AddAnimalForm(data, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("farmer_home_view")
        else:
            print(form.errors)

    return redirect("farmer_home_view")

def book_vet(request):
    if request.POST:
        specialization = request.POST.get('specialization')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        #vets = Vet.objects.filter(specialization = specialization)
        #vet = random.choice(vets)
        data = {}
        data['specialization'] = specialization
        data['subject'] = subject
        data['message'] = message
        #data['vet'] = vet.id        
        data['booked_by'] = request.user        
        form = BookVetForm(data)
        sender_email = request.user.email
        if form.is_valid():
            form.save()
            send_mail(subject, message, 'kutoty004@gmail.com', ['kutoty004@gmail.com'])
            return redirect("farmer_home_view")
        else:
            print(form.errors)
    return redirect("farmer_home_view")