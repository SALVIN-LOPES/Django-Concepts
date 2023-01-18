from functools import partial
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import Student
from .serilizers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io

@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body # json data
        stream = io.BytesIO(json_data) # string data
        python_data = JSONParser().parse(stream) #python dictionary
        id = python_data.get('id',None)
        if id is not None: # id exists -->
            student_data = Student.objects.get(id = id)
            serializer = StudentSerializer(student_data) # complex data type
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type = 'application/json')
    
        student_data = Student.objects.all()
        serializer = StudentSerializer(student_data,many=True) # complex data type
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type = 'application/json')

# json data --> string --> python dictionary --> CDT(serilizers)
    if request.method == 'POST':
        json_data = request.body # json data
        stream = io.BytesIO(json_data) # string data
        python_data = JSONParser().parse(stream) # python dictionary
        serializer = StudentSerializer(data = python_data) # complex data type
        if serializer.is_valid():
            serializer.save()
            res = { 'msg' : 'DATA CREATED SUCCESSFULLY!!' } # object
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
            # return JsonResponse(serilizer,safe = True)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

# json data --> string --> python dictionary --> CDT(serilizers)
    if request.method == 'PUT':
        json_data = request.body # json_data
        stream = io.BytesIO(json_data) # string data
        python_data = JSONParser().parse(stream) #python dictionary
        id = python_data.get('id')
        student_data = Student.objects.get(id = id)
        serializer = StudentSerializer(student_data,data = python_data,partial=True) # complex data type
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'DATA UPDATED SUCCESSFULLY'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')

# json data --> string --> python dictionary --> CDT(serilizers)
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data) # string data
        python_data = JSONParser().parse(stream) # python dictionary
        id = python_data.get('id')
        student_data = Student.objects.get(id = id)
        student_data.delete()
        res = { 'msg' : 'STUDENT DELETED SUCCESSFULLY!!' }
        return JsonResponse(res,safe=False)
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type = 'application/json')
        
