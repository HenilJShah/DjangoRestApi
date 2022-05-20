from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializers
from .models import Student

# Create your views here.
def student_detail(request, id):
    qry = Student.objects.get(id=id)
    serializerdata = StudentSerializers(qry)
    return JsonResponse(serializerdata.data)

def student_detail_all(request):
    qry = Student.objects.all()
    serializerdata = StudentSerializers(qry, many=True)
    json_data = JSONRenderer().render(serializerdata.data)
    return HttpResponse(json_data, content_type ="application/json")