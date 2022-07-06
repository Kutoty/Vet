import uuid
from django.db import models
from accounts.models import Account, Specialization, Vet


class Breed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    farmer = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_created = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)

    def __str__(self):
        return self.name


class AnimalRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    # age = models.CharField(max_length=200)
    birth_date = models.DateTimeField()
    gender = models.CharField(max_length=30)
    weight = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    allergies = models.TextField(null=True, blank=True)
    existing_conditions = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)

    def __str__(self):
        return self.name

class BookVet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=300)
    specialization = models.ForeignKey(Specialization,on_delete=models.CASCADE)
    message = models.TextField()
    vet = models.ForeignKey(Vet,on_delete=models.CASCADE)
    booked_by = models.ForeignKey(Account,on_delete=models.SET_NULL,null=True)
    date_created = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)

    def __str__(self):
        return self.subject