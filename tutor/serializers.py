from django.db import models
from rest_framework import serializers

from .models import Applicant, Teacher

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ('name', 'country', 'phone', 'email', 'gender', 'education', 'experiencedYears', 'expectedSalary', 'preferredCurrency', 'intro', 'resume')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('name', 'country', 'phone', 'email', 'gender', 'education', 'experiencedYears', 'intro')