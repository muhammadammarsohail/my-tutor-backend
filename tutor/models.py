from django.db import models
from django.db.models.fields import CharField, DateField, EmailField, IntegerField
# from django_countries.fields import CountryField

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
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'),('Female','Female')))
    dob = models.DateField()
    transactionMethod = models.CharField(max_length=20, choices=TransactionMethods.choices)
    speaks_english = models.BooleanField()
    # transactionCurrency = 
    def __str__(self):
        return self.student_name
    

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'),('Female','Female')))
    dob = models.DateField()
    transactionMethod = models.CharField(max_length=20, choices=TransactionMethods.choices)
    is_graduate = models.BooleanField(default=False)
    is_master = models.BooleanField(default=False)
    speaks_english = models.BooleanField()
    experiencedYears = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.teacher_name

class Applicant(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'),('Female','Female')))
    # dob = models.DateField()
    # transactionMethod = models.CharField(max_length=20, choices=TransactionMethods.choices)
    # is_graduate = models.BooleanField(default=False)
    education = models.CharField(max_length=50)
    experiencedYears = models.IntegerField(null=True, blank=True)
    # speaks_english = models.BooleanField()
    # has_interviewed = models.BooleanField(default=False)
    expectedSalary = models.IntegerField()
    preferredCurrency = models.CharField(max_length=10)
    intro = models.CharField(max_length=300)
    resume = models.FileField()


    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=20)
    estimatedMonths = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.course_title

    # pass

class Class(models.Model):
    title = models.CharField(max_length=50)
    whatsappGroupLink = models.IntegerField(null=True, blank=True)
    zoomLink = models.IntegerField(null=True, blank=True)
    monthlyFees = models.IntegerField(default=0)
    joiningDate = models.DateField()
    hoursPerMonth = models.IntegerField()
    sessionsPerMonth = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time = models.TimeField()
    language = models.CharField(max_length=20)
    def __str__(self):
        return self.class_title

    # class Teacher(models.Model):
    #     name = models.CharField(max_length=200)
    #     country = models.CharField(max_length=50)
    #     phone = models.CharField(max_length=20)
    #     email = models.EmailField()
    #     gender = models.CharField(max_length=10, choices=(('Male', 'Male'),('Female','Female')))
    #     dob = models.DateField()
    #     transactionMethod = models.CharField(max_length=20, choices=TransactionMethods.choices)
    #     is_graduate = models.BooleanField(default=False)
    #     is_master = models.BooleanField(default=False)
    #     def __str__(self):
    #         return self.teacher_name