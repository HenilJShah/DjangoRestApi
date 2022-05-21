from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.Serializer):
    """name,roll,city"""
    name = serializers.CharField(max_length = 100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)


    # data create
    def create(self, validated_data):
        return Student.objects.create(**validated_data)


    # data update
    def update(self, instance, validated_data):
        print(f"\n\n\nhere i got database object inside instance:\n{instance}\nin validated_data we got request data:\n{validated_data}\n\n\n")
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance