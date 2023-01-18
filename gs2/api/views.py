from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
import io
# Create your views here.

# data --> json --> python dictionary --> complex data(table) --> database
@csrf_exempt
def Student_create(request):
    if request.method == 'POST':
        json_data = request.body # json data from client
        stream = io.BytesIO(json_data) # string data
        python_data = JSONParser().parse(stream) # python dictionary
        serializer = StudentSerializer(data = python_data) # complex data
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'DATA CREATED'} # python data
            json_data = JSONRenderer().render(res) # json data
        # res = { 'msg' : 'DATA NOT CREATED' }
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')
