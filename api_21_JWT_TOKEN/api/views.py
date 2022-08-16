# JWT TOKEN website https://jwt.io/
# how to generate JWT token
# get token
# http POST http://127.0.0.1:8000/gettoken/ username="" password=""
# USER CAN VERIFY TOKEN BY USING == http POST http://127.0.0.1:8000/verifytoken/ token=">>>>>>>>>>>>>>>>>>>"
# USER can generate new token by using refresh token  == http POST http://127.0.0.1:8000/refreshtoken/ refresh=">>>>>>>>>>>>>>>>>>>"
# how to get all data
# http POST http://127.0.0.1:8000/student_api/
# how to authenticate JWT toekn and get data
# http POST http://127.0.0.1:8000/student_api/ 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwNTc5NjA3LCJpYXQiOjE2NjA1NzgwMjUsImp0aSI6IjUyNTMzNTM1M2U3MTQ4MmJhODY5MjE3NGNkNzA3ZWJhIiwidXNlcl9pZCI6MX0.lqI4KDmgoaIeWbJlKHcsGtiRAjlexPUldn3FgnyZewA'
# how to POST data data using jwt token
# http -f POST http://127.0.0.1:8000/student_api/ name=raj roll=22 city=delhi'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwNTc5NjA3LCJpYXQiOjE2NjA1NzgwMjUsImp0aSI6IjUyNTMzNTM1M2U3MTQ4MmJhODY5MjE3NGNkNzA3ZWJhIiwidXNlcl9pZCI6MX0.lqI4KDmgoaIeWbJlKHcsGtiRAjlexPUldn3FgnyZewA'
# how to PUT data data using jwt token
# http PUT http://127.0.0.1:8000/student_api/2/ name=raj roll=22 city=delhi'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwNTc5NjA3LCJpYXQiOjE2NjA1NzgwMjUsImp0aSI6IjUyNTMzNTM1M2U3MTQ4MmJhODY5MjE3NGNkNzA3ZWJhIiwidXNlcl9pZCI6MX0.lqI4KDmgoaIeWbJlKHcsGtiRAjlexPUldn3FgnyZewA'
# how to DELETE data data using jwt token
# http DELETE http://127.0.0.1:8000/student_api/2/ 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwNTc5NjA3LCJpYXQiOjE2NjA1NzgwMjUsImp0aSI6IjUyNTMzNTM1M2U3MTQ4MmJhODY5MjE3NGNkNzA3ZWJhIiwidXNlcl9pZCI6MX0.lqI4KDmgoaIeWbJlKHcsGtiRAjlexPUldn3FgnyZewA'


from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
