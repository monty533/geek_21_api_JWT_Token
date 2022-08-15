# 1 => from admin panel we can generate token

# 2 => from command line we can generate token (python manage.py drf_create_token <username>)

# 3 => user can generate token by itself user have to give username and password
# for ex - http POST http://127.0.0.1:8000/gettoken/ username="user" password="suitor@@gloria" for this we have to install httpie

from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
