from urllib import response
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers

# Create your views here.
@api_view(['GET','POST','PUT','DELETE'])
def Student_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            student_data = Student.objects.get(id = id) # complex data
            serializer = StudentSerializers(student_data)
            return Response(serializer.data)
        student_data =  Student.objects.all()
        serializer = StudentSerializers(student_data,many=True)
        return Response(serializer.data)  

    # python dict --> serilizers -->
    if request.method == 'POST':
        serializer = StudentSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'msg':'POST DATA CREATED SUCCESSFULLY!!' })

        return Response(serializer.errors)
    
    if request.method == 'PUT':
        id = request.data.get('id')
        student_data = Student.objects.get(pk = id)
        serializer = StudentSerializers(student_data,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'STUDENT UPDATED SUCCESSFULLY!'})
        return response(serializer.errors)
    
    if request.method == 'DELETE':
        id = request.data.get('id')
        student_data = Student.objects.get(pk=id)
        student_data.delete()
        return Response({'msg':'STUDENT DELETED SUCCESSFULLY!!'})




