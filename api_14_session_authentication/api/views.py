# modelviewset in drf

from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated] #means those who r authencated
    # permission_classes = [IsAdminUser]  # means staff true can access

    # means user can access if authenticated otherwise read operation will done by user
    # permission_classes = [IsAuthenticatedOrReadOnly]

    # means we have to give the permission from backend [means from admin panel]
    # permission_classes = [DjangoModelPermissions]

    # means we have to give the permission from backend [means from admin panel] but bydefault it will run safe method
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
