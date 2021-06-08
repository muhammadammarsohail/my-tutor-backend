
from django.db.models import fields
from rest_framework import serializers

from .models import Applicant, Class
from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Applicant, Class, Teacher

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ('id', 'name', 'country', 'phone', 'email', 'gender', 'education', 'experiencedYears', 'expectedSalary', 'preferredCurrency', 'intro')


class TrainingClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('title', 'zoomLink', 'joiningDate', 'teacher', 'course', 'time', 'language', 'days')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('name', 'country', 'phone', 'email', 'gender', 'education', 'experiencedYears', 'intro')


class TrainingClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('title', 'zoomLink', 'startingDate', 'teacher', 'course', 'time', 'language','days')

# class No