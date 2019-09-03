from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import HttpResponse

from employee.serializers import EmployeeSerializer
# Create your views here.

class EmployeeViewset(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = EmployeeSerializer