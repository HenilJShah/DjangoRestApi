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

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class StudentDelete(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



# ! === *** group of classes *** === !

# ? List and Create not required id in url
class List_and_Create_Student(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset =  Student.objects.all()
    serializer_class = StudentSerializers

    # fetch data
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # Create data
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# ? Update, Retrieve and Delete required id in 

class update_retrieve_and_delete_student(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset =  Student.objects.all()
    serializer_class = StudentSerializers

    # update complete data
    def put(self,  request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    # update partial data
    def patch(self,  request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # search data(retrieve)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # delete data
    def delete(self, request, *args, **kwargs):
        print("----->>>>",self.queryset)
        print("----->>>>",request)
        print("----->>>>",args)
        print("----->>>>",kwargs)
        return self.destroy(self, request, *args, **kwargs)
