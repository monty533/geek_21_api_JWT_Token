from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
# from yaml import serializer

from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from .models import Student
# Create your views here.


def student_detail(request, pk):
    # stu = Student.objects.get(id=1)
    stu = Student.objects.get(id=pk)
    # print(stu)
    serializer = StudentSerializer(stu)
    # print(serializer)
    # print(type(serializer))
    # print(serializer.data)
    # print(type(serializer.data))
    json_dat = JSONRenderer().render(serializer.data)
    # print(json_dat)
    return HttpResponse(json_dat, content_type='application/json')
    # this is short method and it is used everywhere
    # return JsonResponse(serializer.data)


def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    # json_dat = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_dat)
    return JsonResponse(serializer.data, safe=False)


# in this we have to give safe parameter = False
