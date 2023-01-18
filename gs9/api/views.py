from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Function based API view -->
# @api_view(['POST','GET','PUT','PATCH','DELETE'])
# @api_view(['GET'])
# def hello_world(request):
#     return Response({ 'msg':'HELLO WORLD!!' })

# @api_view(['GET'])
# def hello_world(request):
#     return Response({ 'msg':'HELLO WORLD!!' })

# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({ 'msg':'HELLO WORLD!!' })

@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'POST':
        print(request.data)
        return Response({ 'msg':'POST REQUEST','data':request.data })

    if request.method == 'GET':
        print(request.data)
        return Response({ 'msg':'GET REQUEST','data':request.data  })



