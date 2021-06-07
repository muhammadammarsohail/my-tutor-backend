
from django.db.models import fields
from rest_framework import serializers

from .models import Applicant, Class
from django.db import models
from rest_framework import serializers

from .models import Applicant, Teacher

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ('name', 'country', 'phone', 'email', 'gender', 'education', 'experiencedYears', 'expectedSalary', 'preferredCurrency', 'intro', 'resume')


class TrainingClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('title', 'zoomLink', 'startingDate', 'teacher', 'course', 'time', 'language', 'days')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('name', 'country', 'phone', 'email', 'gender', 'education', 'experiencedYears', 'intro')
