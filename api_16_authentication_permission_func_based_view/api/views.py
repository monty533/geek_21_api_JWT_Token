from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse

# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_details(request, pk=None):  # sourcery skip: avoid-builtin-shadow
    if request.method == 'GET':
        id = pk
        print("id is ", id)
        if id is not None:
            print('monty')
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": "data created"}
            return Response(res)
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = id
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer. is_valid():
            serializer.save()
            res = {"msg": "updated"}
            return Response(res)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = id
        stu = Student.objects.get(pk=id)
        stu.delete()
        res = {"msg": "deleted"}
        return Response(res)
