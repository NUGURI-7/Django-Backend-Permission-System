"""
URL configuration for DjangoProject222 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from DjangoProject222 import settings

urlpatterns = [
     path('user/', include('user.urls')),
     re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT},name='media'),
    # path('role/', include('role.urls')),
    # path('menu/', include('menu.urls')),

]