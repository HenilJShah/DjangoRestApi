from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

from paginationApp.models import Student
from paginationApp.serializer import StudentSerializer


class MyCustomPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'pg'
    page_size_query_param = 'recodes'
    max_page_size = 7


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 6


class MyCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'id'
    cursor_query_param = 'page'


class StudentPaginationsClass(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # pagination_class = MyCustomPagination
    # pagination_class = MyLimitOffsetPagination
    pagination_class = MyCursorPagination
