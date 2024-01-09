from django.contrib import admin
from .models import Post,Categoria
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('criacao','nome','ativo')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','resumo','texto','imagen','category','criacao','ativo')

