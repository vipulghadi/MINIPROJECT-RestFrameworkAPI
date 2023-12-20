from django.shortcuts import render,HttpResponse
import io
from .models import StudentProfile
from .serialization import StudentProfileSeri
# Create your views here.
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import GenericAPIView,ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
@csrf_exempt
def student_api_from_base(request):
    if request.method=="GET":
        
        # if calling from direct website without data
        try:
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            
            if python_data["email"]==None:
                stu=StudentProfile.objects.all()
                seri=StudentProfileSeri(stu,many=True)
                return HttpResponse(JSONRenderer().render(seri.data)
                                ,content_type="application/json")
            else:
                try:
                    stu=StudentProfile.objects.get(email=python_data["email"])
                    seri=StudentProfileSeri(stu)
                    return HttpResponse(JSONRenderer().render(seri.data)
                                ,content_type="application/json")
                except:
                    return HttpResponse(JSONRenderer().render({"msg":"no user exists"})
                                ,content_type="application/json")
        
        except:
            stu=StudentProfile.objects.all()
            seri=StudentProfileSeri(stu,many=True)
            return HttpResponse(JSONRenderer().render(seri.data)
                                ,content_type="application/json")
        
        # agar request is empty then we will show full data
        
        
        ...
    if request.method=="POST":
        try:
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            ## if user allready exist with name
            
        
            if (StudentProfile.objects.filter(email=python_data["email"]).count()!=0):
                return HttpResponse(JSONRenderer().render({"msg":"user allready exist with this email"}),content_type="application/json")
            else:
                seri=StudentProfileSeri(data=python_data)
                if seri.is_valid():
                    seri.save()
                 
                    return HttpResponse(JSONRenderer().render(
                        {"msg":"data added successfully"}),content_type="application/json")
                else:
                 
                    return HttpResponse(JSONRenderer().render(
                        {"msg":"invalid data!","error":seri.errors}),content_type="application/json")
            
        except Exception as e:
       
            return HttpResponse(JSONRenderer().render(
                        {"msg":"error!"}),content_type="application/json")
            
    if request.method=="PUT":
        try:
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            ## if user allready exist with name
            
            print(1)
            if (StudentProfile.objects.filter(email=python_data["email"]).count()==0):
                print(2)
                return HttpResponse(JSONRenderer().render({"msg":"user does not exist"}),content_type="application/json")
            else:
                print(3)
                stu=StudentProfile.objects.get(email=python_data["email"])
                print(stu)
                print(4)
                seri=StudentProfileSeri(stu,data=python_data,partial=True)
                print(seri)
                if seri.is_valid():
                    print(5)
                    seri.save()
                    print("saved")
                    return HttpResponse(JSONRenderer().render(
                        {"msg":"data updated successfully"}),content_type="application/json")
                
                else:
                    return HttpResponse(JSONRenderer().render(
                        {"msg":"invalid data!"}),content_type="application/json")
            
        except Exception as e:
            print(e)
            return HttpResponse(JSONRenderer().render(
                        {"msg":"error!"}),content_type="application/json")
    if request.method=="DELETE":
        try:
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            ## if user allready exist with name
            
            if (StudentProfile.objects.filter(name=python_data["name"],
                                             email=python_data["email"]).count()==0):
                return HttpResponse(JSONRenderer().render({"msg":"user does not exists"}),content_type="application/json")
            
            else:
                StudentProfile.objects.get(name=python_data["name"],
                                           email=python_data["email"]).delete()
                 
                return HttpResponse(JSONRenderer().render(
                        {"msg":"deleted successfully"}),content_type="application/json")
                
        except Exception as e:
            return HttpResponse(JSONRenderer().render(
                        {"msg":"error!"}),content_type="application/json")


@api_view(["GET","POST","DELETE","PUT"])
def student_api_api_view(request):

    if request.method=="GET":
        print(1)
        try:
            python_data=request.data
            if python_data["email"]==None:
                print(2)
                stu=StudentProfile.objects.all()
                seri=StudentProfileSeri(stu,many=True)
                return Response(data=seri.data
                                )
            else:
                try:
                    print(3)
                    stu=StudentProfile.objects.get(email=python_data["email"])
                    seri=StudentProfileSeri(stu)
                    return Response((seri.data)
                                )
                except:
                    print(4)
                    return Response(data=({"msg":"no user exists"})
                               )
        
        except:
            print(5)
            stu=StudentProfile.objects.all()
            seri=StudentProfileSeri(stu,many=True)
            return Response(seri.data
                                )
        
        # agar request is empty then we will show full data
        
        
    if request.method=="POST":...
    if request.method=="PUT":...
    if request.method=="DELETE":...
    
    
class Student_Generic_Mixin_get(GenericAPIView,ListModelMixin):
    queryset=StudentProfile.objects.all()
    serializer_class=StudentProfileSeri
    
    def get(self,request,*args,**qwargs):
        return self.list(request,*args,**qwargs)


class Student_Generic_Mixin_post(GenericAPIView,CreateModelMixin):
    queryset=StudentProfile.objects.all()
    serializer_class=StudentProfileSeri
    
    def post(self,request,*args,**qwargs):
        return self.create(request,*args,**qwargs)

class Student_Generic_Mixin_retrive(GenericAPIView,RetrieveModelMixin):
    
    queryset=StudentProfile.objects.all()
    serializer_class=StudentProfileSeri
    
    
    def get(self,request,*args,**qwargs):
        return self.retrieve(request,*args,**qwargs)
    
    
class Concrete_List(ListAPIView):
    queryset=StudentProfile.objects.all()
    serializer_class=StudentProfileSeri

    
class Concrete_Retrive(RetrieveAPIView):
    queryset=StudentProfile.objects.all()
    serializer_class=StudentProfileSeri
        
class Concrete_Post(CreateAPIView):
    queryset=StudentProfile.objects.all()
    serializer_class=StudentProfileSeri
        
class Concrete_Update(UpdateAPIView):
    queryset=StudentProfile.objects.all()
    serializer_class=StudentProfileSeri
    
class Concrete_Destroy(DestroyAPIView):
    queryset=StudentProfile.objects.all()
    serializer_class=StudentProfileSeri
    
    
class ClassBasedModelViewset(ModelViewSet):
    queryset=StudentProfile.objects.all()
    serializer_class=StudentProfileSeri
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated,]
    
class ClassBasedModelViewsetReadOnly(ReadOnlyModelViewSet):
    queryset=StudentProfile.objects.all()
    serializer_class=StudentProfileSeri
    
    
        