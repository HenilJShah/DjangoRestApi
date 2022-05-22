from django.http import JsonResponse
from rest_framework import serializers
from .models import Student

# * 3th. Validators level
def not_start_with_number(value):
    if value[0].lower() != "i":
        raise serializers.ValidationError('Name should be start with I')


class StudentSerializers(serializers.Serializer):
    """ name,  roll, city """

    # ? here the no validation
    # name = serializers.CharField(max_length = 100)

    # ! here the validation apply
    name = serializers.CharField(max_length=100, validators=[not_start_with_number])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    # data create

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    # data update

    def update(self, instance, validated_data):
        print(
            f"\n\n\nhere i got database object inside instance:\n{instance}\nin validated_data we got request data:\n{validated_data}\n\n\n")
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    # there is 3 type of validation

    # TODO: 1st. felid level validation
    def validate_roll(self, value):
        if value >= 100:
            raise serializers.ValidationError("roll no not accept gre 100")
        return value

    # TODO: 2nd. object level validation
    def validate(self, data):
        # print(f"here name is :{data.get('name')}")
        # print(f"here roll is :{data.get('roll')}")
        # print(f"here city is :{data.get('city')}")
        if data.get('name').lower() == data.get('name'):
            # print("name accept")
            pass
        else:
            raise serializers.ValidationError(
                "name start with lower char...!!")
        return super().validate(data)

    # TODO: 3rd define on top