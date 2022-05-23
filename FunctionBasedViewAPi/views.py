from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializers
from .models import Student
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def FunctionBasedCRUDApi(request):
    if request.method == "GET":
        id = request.data.get("id")
        if id is not None:
            studata = Student.objects.get(id=id)
            serializer = StudentSerializers(studata)
            return Response(serializer.data, status=status.HTTP_200_OK)
        stuall = Student.objects.all()
        serializer = StudentSerializers(stuall, many=True)
        print("serial:", serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if  request.method == "POST":
        serial = StudentSerializers(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response({"msg":f"Data name:{request.data.get('name')} save !!"}, status=status.HTTP_201_CREATED)
        return Response({"msg":serial.errors}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PUT":
        id = request.data.get('id')
        stuid =Student.objects.get(id=id)
        serializer = StudentSerializers(stuid, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":f"recode >complete< name={request.data.get('name')} updated"},status=status.HTTP_200_OK)
        return Response({"msg":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    if request.method == "PATCH":
        id = request.data.get('id')
        stuid =Student.objects.get(id=id)
        serializer = StudentSerializers(stuid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":f"recode >partial< name={request.data.get('name')} updated"},status=status.HTTP_200_OK)
        return Response({"msg":serializer.errors})

    if request.method == 'DELETE':
        stuid = request.data.get('id')
        Student.objects.get(id=stuid).delete()
        return Response({'msg':f"recode deleted"}, status=status.HTTP_200_OK)