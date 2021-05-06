from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import registration_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_auth_token, name='login'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('api/', include('users.urls')),
    path('api/', include('articles.urls')),
    path("auth/",
         include("rest_framework.urls")),
]