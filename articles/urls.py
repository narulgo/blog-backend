from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ArticleViewSet

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]