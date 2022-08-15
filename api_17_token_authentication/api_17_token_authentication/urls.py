from django.contrib import admin
from django.urls import path, include
from api import views
from api.auth import CustomAuthToken
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('student_api', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('auth/', include("rest_framework.urls", namespace='rest_framework')),

    # for generate token for the user
    # this is used when user creates token by itself
    # path('gettoken/', obtain_auth_token),

    # this is used when user creates token by itself and this will give all details of the user
    path('gettoken/', CustomAuthToken.as_view()),
]
