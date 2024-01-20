from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostViewset,CategoriaViewset

router = SimpleRouter()
router.register('post',PostViewset)
router.register('categoria',CategoriaViewset)