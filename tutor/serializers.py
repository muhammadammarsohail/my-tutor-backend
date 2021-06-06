from rest_framework import serializers

from .models import Applicant

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ('name', 'country', 'phone', 'email', 'gender', 'education', 'experiencedYears', 'expectedSalary', 'preferredCurrency', 'intro', 'resume')
