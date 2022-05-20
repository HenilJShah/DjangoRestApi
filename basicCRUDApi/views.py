import io
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Student

from .serializers import StudentSerializers

# Create your views here.


@csrf_exempt
def createStudent(request):
    if request.method == "GET":
        data = Student.objects.all()
        studata = StudentSerializers(data, many=True)
        return HttpResponse(JSONRenderer().render(studata.data), content_type='application/json')

    if request.method == "POST":
        bodydata = request.body
        serialize = StudentSerializers(data = JSONParser().parse(io.BytesIO(bodydata)))
        if serialize.is_valid():
            serialize.save()
            return JsonResponse({'msg':"data save"})
