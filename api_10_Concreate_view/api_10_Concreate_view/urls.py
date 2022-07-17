"""api_8_class_based_view URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    # concreate view
    path('admin/', admin.site.urls),
    path('stu_api/', views.student_List_APIView.as_view()),
    path('stu_api/create/', views.student_Create_APIView.as_view()),
    path('stu_api/retrieve/<int:pk>/', views.student_Retrieve_APIView.as_view()),
    path('stu_api/update/<int:pk>/', views.student_Update_APIView.as_view()),
    path('stu_api/destroy/<int:pk>/',
         views.student_Destroy_APIView.as_view()),
    # concreate view with less code
    path('stu_app/', views.student_List_create_APIView.as_view()),
    path('stu_app/<int:pk>/', views.student_retrieve_update_APIView.as_view()),
    path('stu_app/rd/<int:pk>/', views.student_retrieve_destroy_APIView.as_view()),
    path('stu_app/rdu/<int:pk>/',
         views.student_retrieve_update_destroy_APIView.as_view()),

    # concreate view aur with less code
    path('stu_st/', views.student_listcreate_APIView.as_view()),
    path('stu_st/<int:pk>/',
         views.student_retrieveupdatedestroy_APIView.as_view()),
]
