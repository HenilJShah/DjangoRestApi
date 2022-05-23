from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializers
from rest_framework import status

# Create your views here.


class ClassBasedCRUDApi(APIView):
    def get(self, request, format=None):
        if request.data.get('id'):
            studata = Student.objects.get(id=request.data.get('id'))
            serializer = StudentSerializers(studata)
            return Response(serializer.data, status=status.HTTP_200_OK)
        studata = Student.objects.all()
        serializer = StudentSerializers(studata, many=True)   
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response({'msg':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # partial update
    def patch(self, request, format=None):
        stu = Student.objects.get(id=request.data.get('id'))
        serializer = StudentSerializers(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'update successfully'}, status=status.HTTP_200_OK)
        return Response({'msg':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # complete update
    def put(self, request, format=None):
        stu = Student.objects.get(id=request.data.get('id'))
        serializer = StudentSerializers(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'update successfully'}, status=status.HTTP_200_OK)
        return Response({'msg':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, format=None):
        Student.objects.get(id = request.data.get('id')).delete()
        return Response({'msg':'delete successfully'}, status=status.HTTP_200_OK)
