from django import forms
from django.db.models import fields
from . models import Breed, AnimalRecord,BookVet
from accounts.models import Specialization


class BreedRegistrationForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = ['name', 'farmer']


class AddSpecializationForm(forms.ModelForm):
    class Meta:
        model = Specialization
        fields = ['name']


class AddAnimalForm(forms.ModelForm):
    class Meta:
        model = AnimalRecord
        fields = ['breed', 'farmer', 'name', 'birth_date',
                  'gender', 'weight', 'photo', 'allergies', 'existing_conditions']

class BookVetForm(forms.ModelForm):
    class Meta:
        model = BookVet
        fields = ['subject','booked_by','specialization','message','vet']