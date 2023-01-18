
from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Model object --> Single Student Data : 

# Student single data : 
def student_detail(request,pk):
    stu = Student.objects.get(id = pk) # complex data
    # print("STU:",stu)
    stu_serilizer = StudentSerializer(stu,many=False) # python dictionary
    # print("stu_serilizer:",stu_serilizer.data)
    # json_data = JSONRenderer().render(stu_serilizer.data) # json format
    # print("json_data:",json_data)

    # return HttpResponse(json_data,content_type = 'application/json')
    return JsonResponse(stu_serilizer.data)

# Query Set --> All Student Data : 
def student_list(request):
    stu = Student.objects.all() # complex data
    # print("STU:",stu)
    stu_serilizer = StudentSerializer(stu,many=True) # python dictionary
    # print("stu_serilizer:",stu_serilizer.data)
    # json_data = JSONRenderer().render(stu_serilizer.data) # json format
    # print("json_data:",json_data)

    return JsonResponse(stu_serilizer.data,safe=False)

