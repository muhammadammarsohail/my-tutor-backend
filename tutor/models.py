from django.db import models
from django.db.models.fields import CharField, DateField, EmailField, IntegerField
from django_countries.fields import CountryField

class TransactionMethods(models.Choices):
    BT = 'Bank Transfer'
    Paypal = 'Paypal'
    Payoneer = 'Payoneer'
    WU = 'Western Union'
    RIA = 'RIA'
    MG = 'Moneygram'

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    country = CountryField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'),('Female','Female')))
    dob = models.DateField()
    transactionMethod = models.CharField(max_length=20, choices=TransactionMethods.choices)
    # transactionCurrency = 
    

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    country = CountryField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'),('Female','Female')))
    dob = models.DateField()
    transactionMethod = models.CharField(max_length=20, choices=TransactionMethods.choices)
    is_Graduate = models.BooleanField(default=False)
    is_Master = models.BooleanField(default=False)

class Course(models.Model):
    Title = models.CharField(max_length=20)
    EstimatedMonths = models.IntegerField(null=True, blank=True)

    # pass

class Class(models.Model):
    whatsappGroupLink = models.IntegerField(null=True, blank=True)
    zoomLink = models.IntegerField(null=True, blank=True)
    monthlyFees = models.IntegerField(default=0)
    joiningDate = models.DateField()
    hoursPerMonth = models.IntegerField()
    sessionsPerMonth = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    