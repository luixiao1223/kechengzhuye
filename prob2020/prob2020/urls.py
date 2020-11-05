"""prob2020 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .import views

urlpatterns = [
    path('main/',views.main_page),
    path('main/quiz01pdf', views.quiz01pdf),
    path('main/quiz02', views.quiz02),
    path('main/quiz01ans', views.quiz01ans),
    path('main/quiz02ans', views.quiz02ans),
    path('main/tips01pdf', views.tips01pdf),
    path('main/tips02', views.tips02),
    path('main/ans01pdf', views.ans01pdf),
    path('main/ans02', views.ans02),
    path('main/ppt01', views.ppt01),
    path('main/ppt02', views.ppt02),
    path('main/ppt03', views.ppt03),
    path('main/ppt04', views.ppt04),
    path('main/test01', views.test01),
    path('main/test01ans', views.test01ans),
    path('admin/', admin.site.urls),
]
