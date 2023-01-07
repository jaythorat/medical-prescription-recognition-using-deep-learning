from django.contrib import admin
from django.urls import path,include
from sunhacksapp import views

urlpatterns = [
    path('',views.index,name='index'),
    # path("fileupload/",views.fileupload,name='fileupload'),
]
