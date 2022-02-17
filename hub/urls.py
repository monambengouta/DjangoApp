from unicodedata import name
from django.urls import path
from .views import homePage ,student_list,student_details

urlpatterns = [
    path('home/',homePage,name='home'),
    path('liststudent/',student_list,name='student_list'),
    path('getstudent/<int:id>',student_details,name='student_details'),
]