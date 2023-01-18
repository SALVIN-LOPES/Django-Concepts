
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializers

# Create your views here.
class StudentAPI(APIView):
    def get(self,request,pk=None,format=None):
        if pk is not None: 
            student_data = Student.objects.get(id=pk) # complex data
            serializer = StudentSerializers(student_data)
            return Response(serializer.data)
        student_data =  Student.objects.all()
        serializer = StudentSerializers(student_data,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = StudentSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'msg':'POST DATA CREATED SUCCESSFULLY!!' })

        return Response(serializer.errors)
    
    def put(self,request,pk=None,format=None):
        student_data = Student.objects.get(id=pk)
        serializer = StudentSerializers(student_data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'STUDENT COMPLETE UPDATED SUCCESSFULLY!'})
        return Response(serializer.errors)
    
    def patch(self,request,pk=None,format=None):
        student_data = Student.objects.get(id=pk)
        serializer = StudentSerializers(student_data,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'STUDENT PARTIAL UPDATED SUCCESSFULLY!'})
        return Response(serializer.errors)
    
    def delete(self,request,pk=None,format=None):
        student_data = Student.objects.get(pk)
        student_data.delete()
        return Response({'msg':'STUDENT DELETED SUCCESSFULLY!!'})




















# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def Student_api(request,pk=None):
#     if request.method == 'GET':
#         if pk is not None: 
#             student_data = Student.objects.get(id=pk) # complex data
#             serializer = StudentSerializers(student_data)
#             return Response(serializer.data)
#         student_data =  Student.objects.all()
#         serializer = StudentSerializers(student_data,many=True)
#         return Response(serializer.data)  

#     # python dict --> serilizers -->
#     if request.method == 'POST':
#         serializer = StudentSerializers(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({ 'msg':'POST DATA CREATED SUCCESSFULLY!!' })

#         return Response(serializer.errors)
    
#     if request.method == 'PUT':
#         student_data = Student.objects.get(pk)
#         serializer = StudentSerializers(student_data,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'STUDENT COMPLETE UPDATED SUCCESSFULLY!'})
#         return response(serializer.errors)
    
#     if request.method == 'PATCH':
#         student_data = Student.objects.get(pk)
#         serializer = StudentSerializers(student_data,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'STUDENT PARTIAL UPDATED SUCCESSFULLY!'})
#         return response(serializer.errors)
    
#     if request.method == 'DELETE':
#         student_data = Student.objects.get(pk)
#         student_data.delete()
#         return Response({'msg':'STUDENT DELETED SUCCESSFULLY!!'})




