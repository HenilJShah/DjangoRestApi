from rest_framework import viewsets
from ViewSetApi.models import Student
from ViewSetApi.serializers import StudentSerializers


# Create your views here.
class StudentApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
