from rest_framework import serializers
from .models import Post,Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id','nome']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id",'titulo','resumo','imagem','texto','category']
