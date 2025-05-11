from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LivroViewSet, ProgressoLeituraViewSet

router = DefaultRouter()
router.register(r'livros', LivroViewSet, basename='livro')
router.register(r'progresso', ProgressoLeituraViewSet, basename='progresso')

urlpatterns = [
    path('', include(router.urls)),
]
