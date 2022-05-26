from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

from .serializers import StudentSerializers
from .models import Student


# Create your views here.
# fetch all
class StudentApi(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# create 
class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# update 
class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

# retrieve 
class StudentRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def post(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

