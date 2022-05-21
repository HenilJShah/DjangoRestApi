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
def CrudStudent(request):
    # fetch data
    if request.method == "GET":
        bodydata = request.body
        bdata = io.BytesIO(bodydata)
        pythondata = JSONParser().parse(bdata)
        id = pythondata.get('id')
        if id is not None:
            studata = Student.objects.get(id=id)
            serializer = StudentSerializers(studata)
            return JsonResponse(serializer.data)


    # update
    if request.method == "PUT":
        bodydata = request.body
        bdata = io.BytesIO(bodydata)
        python_data = JSONParser().parse(bdata)
        stuid = python_data.get('id')
        qrydata = Student.objects.get(id = stuid)
        serialize = StudentSerializers(qrydata, data=python_data, partial=True)
        if serialize.is_valid():
            serialize.save()
        else:
            print("error==>", serialize.errors)

    if request.method == "DELETE":
        delete_id = io.BytesIO(request.body)
        id = JSONParser().parse(delete_id).get('id')
        Student.objects.get(id=id).delete()
        return JsonResponse({"msg":"delete data"}, safe=False)
    

    # create data
    if request.method == "POST":
        bodydata = request.body
        serialize = StudentSerializers(
            data=JSONParser().parse(io.BytesIO(bodydata)))
        if serialize.is_valid():
            serialize.save()
            return JsonResponse({'msg': "data save"})
        else:
            print(serialize.errors)
            return JSONRenderer().render({'msg': serialize.errors})
    data = Student.objects.all()
    studata = StudentSerializers(data, many=True)
    return HttpResponse(JSONRenderer().render(studata.data), content_type='application/json')
