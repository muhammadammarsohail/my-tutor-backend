from tutor.models import Applicant
from django.db import models
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.views import generic
from .serializers import ApplicantSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from tutor import serializers



def index(request):
    return HttpResponse("Hello, world. You're at the tutor index.")

class ApplicantView(APIView):
    def post(self, request):
        serializer = ApplicantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        applicants = Applicant.objects.filter(id=pk)
        serializer = ApplicantSerializer(applicants, many=True)
        return Response(serializer.data)

class AllApplicantView(APIView):
    def post(self, request):
        serializer = ApplicantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        applicants = Applicant.objects.all()        
        serializer = ApplicantSerializer(applicants, many=True)
        return Response(serializer.data)