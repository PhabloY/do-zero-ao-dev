"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from blog import views as blog_views
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from home import views as home_views


def home(request):
    print('home')
    return HttpResponse('home')


def blog(requests):
    print('blog')
    return HttpResponse('blog')


urlpatterns = [
    path('', home_views.home),
    path('admin/', blog_views.blog),
    path('blog/', admin.site.urls),
]
