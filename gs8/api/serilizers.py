from wsgiref.validate import validator
from django.forms import ValidationError
from rest_framework import serializers
from .models import Student

# validators --> // 1
# def start_with_r(value):
#     if value[0].lower() == 'r':
#         return value
#     raise serializers.ValidationError("Name should start with r")



class StudentSerializer(serializers.ModelSerializer):
    def start_with_r(value):
        if value[0].lower() == 'r':
            return value
        raise serializers.ValidationError("Name should start with r")

    name = serializers.CharField(validators = [start_with_r])
    class Meta:
        model = Student
        fields = ['id','name','roll','city']

    # -----------FIELD LEVEL VALIDATION-------------
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError("seats are full")
        return value
    
    def validate(self,data):
        name = data.get('name')
        city = data.get('city')
        #condition -->
        if name.lower() == 'joral lopes' and city.lower() != 'nagpur':
            raise serializers.ValidationError("joral belong to nagpur city!!")
        return data

    













    # ---------------FIELD LEVEL-->VALIDATION : // 2----------------
    # if need to validate only particular fields
    # def validate_roll(self,value):
    #     if value >= 200:
    #         raise serializers.ValidationError("seats full ! better luck next time")
    #     return value
    
    # ---------------OBJECT LEVEL-->VALIDATION // 3----------------
    # if need to validate all fields
    # def validate(self,data):
    #     name = data.get('name')
    #     city = data.get('city')
    #     #condition -->
    #     if name.lower() == 'joral lopes' and city.lower() != 'nagpur':
    #         raise serializers.ValidationError("joral belong to nagpur city!!")
    #     return data

    # def create(self,validated_data):
    #     return Student.objects.create(**validated_data)

    # def update(self,instance,validated_data):
    #     instance.name = validated_data.get('name',instance.name)
    #     instance.roll = validated_data.get('roll',instance.roll)
    #     instance.city = validated_data.get('city',instance.city)

    #     instance.save()
    #     return instance
