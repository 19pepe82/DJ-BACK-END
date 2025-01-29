
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from . import views


urlpatterns = [
 
   # path('api-auth/', include('rest_framework.urls')),
     path('', views.getData),
       path('add/', views.addItem),
]