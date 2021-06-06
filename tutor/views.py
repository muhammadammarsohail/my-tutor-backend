from django.db import models
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.views import generic
from .serializers import ApplicantSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



def index(request):
    return HttpResponse("Hello, world. You're at the tutor index.")

class ApplicantView(APIView):
    def post(request):
        serializer = ApplicantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)