from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response 

# Create your views here.


class userview(APIView):
    def get(self,request):
        a=User.objects.all()
        s=Userserializer(a,many=True)
        return Response(s.data)
    
    def post(self,request):
        
         a = Userserializer(data=request.data)
         if a.is_valid():
            a.save()
            return Response({"Msg": "Registration Completed"})
         else:
            return Response({"Msg": "Registration Failed"})





class post_allview(APIView):
    def get(self,request):
        a=Post.objects.all()
        s=PostSerializer(a,many=True)
        return Response(s.data)
    
    def post(self, request):
     a = PostSerializer(data=request.data)
     if a.is_valid():
        a.save()
        return Response({'Msg': 'Item added'})
     




class postview(APIView):
 

    def get(self, request, **kwargs):
        ide = kwargs.get('id')
        a = Post.objects.get(id=ide)
        if a.status=='Public':
            b = PostSerializer(a)
            return Response(b.data)
        if a.status !='Public' and a.user==request.user:
            b = PostSerializer(a)
            return Response(b.data)
        else:
            return Response({'Msg':'Private Post'})
        
       

    def put(self, request, **kwargs):
        ide = kwargs.get('id')
        b = Post.objects.get(id=ide)
        if b.user==request.user:
         a = PostSerializer(instance=b, data=request.data)
         if a.is_valid():
            a.save()
            return Response(a.data)
        else:
            return Response({'Msg':'Not your post'})
        
    def delete(self, request, **kwargs):
        ide = kwargs.get('id')
        a = Post.objects.get(id=ide)
        if a.user==request.user:
          a.delete()
          return Response({'Msg': 'Deleted'})
        else:
           return Response({'Msg':'Not your post'})
           
    

class likeallview(APIView):

    def get(self,request):
        a=Likes.objects.all()
        s=Likeserializer(a,many=True)
        return Response(s.data)
    
    def post(self, request):

        a = Likeserializer(data=request.data)
        if a.is_valid():
            a.save()
            return Response({'MSG': 'Like Added'})
        


class likeview(APIView):


    def get(self, request, **kwargs):
        ide = kwargs.get('id')
        a = Likes.objects.get(id=ide)
        b = Likeserializer(a)
        return Response(b.data)



    def put(self, request,**kwargs):
        ide = kwargs.get('id')
        b =  Likes.objects.get(id=ide)
        a = Likeserializer(instance=b, data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data)
        
    def delete(self, request, **kwargs):
        ide = kwargs.get('id')
        a =  Likes.objects.get(id=ide)
        a.delete()
        return Response({'MSG': 'Like Deleted'})
