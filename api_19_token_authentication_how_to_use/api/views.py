# how to use token authentication
# this url is for get
# http http://127.0.0.1:8000/student_api/ 'Authorization:Token ab7b8fa2cee9184b3dd203e0333b38472b7b21b3'
# this url is for post
# http -f POST http://127.0.0.1:8000/student_api/ name=jay roll=989 city=sikandrabad 'Authorization:Token ab7b8fa2cee9184b3dd203e0333b38472b7b21b3'
# this url is for put
# http PUT http://127.0.0.1:8000/student_api/2/ name=jayiu roll=9389 city=ddsikandrabad 'Authorization:Token ab7b8fa2cee9184b3dd203e0333b38472b7b21b3'
# this url is for delete
# http DELETE http://127.0.0.1:8000/student_api/2/ 'Authorization:Token ab7b8fa2cee9184b3dd203e0333b38472b7b21b3'


from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
