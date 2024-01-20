from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from .models import Post,Categoria
from .serializers import PostSerializer,CategoriaSerializer
# Create your views here.

class CategoriaViewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    @action(detail=True,methods=["GET"])
    def posts(self,request,pk=None):    
        posts=Post.objects.filter(category_id=pk)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self,request):
        title = self.request.query_params.get('title')        
        if title != None:            
            posts = Post.objects.filter(titulo=title)
            serializer = PostSerializer(posts,many=True)
            return Response(serializer.data)
        post =Post.objects.all() 
        serializer = PostSerializer(post,many=True)
        return Response(serializer.data)
       
