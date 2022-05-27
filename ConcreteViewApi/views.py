from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import StudentSerializers
from .models import Student

# Create your views here.

# method = [GET]
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

# method = [POST]
class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

# method = [GET]
class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

# method = [PUT, PATCH]
class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

# method = [DELETE]
class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

# method = [GET = 'fetch all recode', POST = 'create recode']
class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

# method = [GET = 'fetch all recode', {PUT, PATCH} = 'Update recode']
class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

# method = [GET = 'fetch all recode', {PUT, PATCH} = 'Update recode', DELETE = 'delete recode']
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers



# CRUD
# method = [GET = 'fetch all recode', POST = 'create recode']
class StudentListCreateCRUD(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

# method = [GET = 'fetch all recode', {PUT, PATCH} = 'Update recode', DELETE = 'delete recode']
class StudentRetrieveUpdateDestroyCRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

