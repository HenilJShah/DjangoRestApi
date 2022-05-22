import io
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializers
from django.utils.decorators import method_decorator

# Create your views here.


@method_decorator(csrf_exempt, name="dispatch")
class CrudStudent(View):
    # fetch data
    def get(self, request, *args, **kwargs):
        bodydata = request.body
        if bodydata:
            bdata = io.BytesIO(bodydata)
            pythondata = JSONParser().parse(bdata)
            id = pythondata.get('id')
            if id is not None:
                studata = Student.objects.get(id=id)
                serializer = StudentSerializers(studata)
                return JsonResponse(serializer.data)
        data = Student.objects.all()
        studata = StudentSerializers(data, many=True)
        return HttpResponse(JSONRenderer().render(studata.data), content_type='application/json')

    # create data
    def post(self, request, *args, **kwargs):
        bodydata = request.body
        byData = io.BytesIO(bodydata)
        pythondata = JSONParser().parse(byData)
        serialize = StudentSerializers(data=pythondata)
        if serialize.is_valid():
            serialize.save()
            return JsonResponse({'msg': "data save"})
        return JsonResponse({'msg': serialize.errors})

    # update data
    def put(self, request, *args, **kwargs):
        bodydata = request.body
        bdata = io.BytesIO(bodydata)
        python_data = JSONParser().parse(bdata)
        stuid = python_data.get('id')
        qrydata = Student.objects.get(id=stuid)
        serialize = StudentSerializers(qrydata, data=python_data, partial=True)
        if serialize.is_valid():
            serialize.save()
        return JsonResponse(serialize.errors)

    # delete data
    def delete(self, request, *args, **kwargs):
        delete_id = io.BytesIO(request.body)
        id = JSONParser().parse(delete_id).get('id')
        Student.objects.get(id=id).delete()
        return JsonResponse({"msg": "delete data"})
