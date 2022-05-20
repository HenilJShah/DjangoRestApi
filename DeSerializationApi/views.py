import io
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def CreateData(request):
    if request.method == "POST":
        json_data = request.body
        iodata = io.BytesIO(json_data)
        # print("------------->>",io.BytesIO(json_data).read())
        pythondata = JSONParser().parse(iodata)
        serializer = StudentSerializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            response = {"msg": "data save"}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content='application/json')
