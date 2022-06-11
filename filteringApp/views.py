from django.shortcuts import render

# Create your views here.
from django_filters.filterset import filterset_factory
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.relations import method_overridden
from rest_framework.views import APIView

from filteringApp.models import Student
from filteringApp.serializer import StudentSerializer


# class StudentList(APIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         return Student.objects.filter(passby=user)
#

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('roll', 'city', 'passby')


class StudentSeach(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (SearchFilter,)

    # normal search
    # search_fields = ('roll', 'city', 'passby', 'id')

    # regex search
    # "^" means start with
    # "=" exact match
    # '@' full-text search
    # "$" regex search

    search_fields = ('^roll', '^city', '^passby', '^id')


class StudentOrdering(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['name']
