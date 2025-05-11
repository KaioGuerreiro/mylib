from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LivroViewSet, ProgressoLeituraViewSet

router = DefaultRouter()
router.register(r'livros', LivroViewSet)
router.register(r'progresso', ProgressoLeituraViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
