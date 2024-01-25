from rest_framework import serializers
from .models import Post,Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id','nome']

class PostRetrieveSerializer(serializers.ModelSerializer):
    category = CategoriaSerializer()
    class Meta:
        model = Post
        fields = ["id",'titulo','resumo','imagem','texto','category']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id",'titulo','resumo','imagem','texto','category']
