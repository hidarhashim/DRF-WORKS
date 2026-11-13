"""
URL configuration for movie_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from rest_framework.views import APIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create',views.Moviecreate.as_view()),
    path('list',views.Movielist.as_view()),
    path('retrieve/<int:i>',views.Movieretrieve.as_view()),
    path('update/<int:i>',views.Movieupdate.as_view()),
    path('partialupdate/<int:i>',views.Moviepartialupdate.as_view()),
    path('delete/<int:i>',views.Moviedelete.as_view()),
    path('search',views.SearchAPIView.as_view()),
    path('register',views.RegisterAPIView.as_view())
]
