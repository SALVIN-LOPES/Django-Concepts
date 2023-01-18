# GenericAPIView and Model Mixin -->
from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

# Create your views here.
class StudentList(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class StudentUpdatePartial(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class StudentDelete(GenericAPIView,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)




















# class StudentAPI(APIView):
#     def get(self,request,pk=None,format=None):
#         if pk is not None: 
#             student_data = Student.objects.get(id=pk) # complex data
#             serializer = StudentSerializers(student_data)
#             return Response(serializer.data)
#         student_data =  Student.objects.all()
#         serializer = StudentSerializers(student_data,many=True)
#         return Response(serializer.data)

#     def post(self,request,format=None):
#         serializer = StudentSerializers(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({ 'msg':'POST DATA CREATED SUCCESSFULLY!!' })

#         return Response(serializer.errors)
    
#     def put(self,request,pk=None,format=None):
#         student_data = Student.objects.get(id=pk)
#         serializer = StudentSerializers(student_data,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'STUDENT COMPLETE UPDATED SUCCESSFULLY!'})
#         return Response(serializer.errors)
    
#     def patch(self,request,pk=None,format=None):
#         student_data = Student.objects.get(id=pk)
#         serializer = StudentSerializers(student_data,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'STUDENT PARTIAL UPDATED SUCCESSFULLY!'})
#         return Response(serializer.errors)
    
#     def delete(self,request,pk=None,format=None):
#         student_data = Student.objects.get(pk)
#         student_data.delete()
#         return Response({'msg':'STUDENT DELETED SUCCESSFULLY!!'})



















