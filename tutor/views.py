from django.db import models
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.views import generic
from .serializers import ApplicantSerializer, TeacherSerializer, TrainingClassSerializer
from .models import Applicant, Class, Teacher

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from django.forms.models import model_to_dict




def index(request):
    return HttpResponse("Hello, world. You're at the tutor index.")

class ApplicantView(APIView):
    def post(request):
        serializer = ApplicantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class Hire(APIView):

@api_view(['Get',])
# @renderer_classes(('TemplateHTMLRenderer, JSONRenderer'))
def hire(request, pk):
    applicant = Applicant.objects.filter(id=pk).first()
    serializer = TeacherSerializer(data = model_to_dict(applicant))
    if serializer.is_valid():
        serializer.save()
        print("Hired")
        deleteHired(request, applicant)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deleteHired(request, applicant):
    applicant.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    
class TrainingClassesView(APIView):
    def get(self, request):
        classes = Class.objects.filter(is_training=True)
        serializer = TrainingClassSerializer(classes, many=True)
        return Response(serializer.data)