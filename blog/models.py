from django.db import models

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

class Categoria(Base):
    nome = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

        def __str__(self):
            return {self.nome}


class Post(Base):
    titulo = models.CharField(max_length=30)
    resumo = models.CharField(max_length=255)
    texto = models.TextField()
    imagen= models.ImageField(upload_to="img")
    category = models.ForeignKey(Categoria,related_name="posts",on_delete=models.CASCADE)    

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"O post{self.titulo} pertence a categoria {self.category}"