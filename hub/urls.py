from unicodedata import name
from django.urls import path
from .views import homePage ,student_list,student_details,StudentListView,StudentDetailView,createStudent,addStudentForm,StudentCreateView

urlpatterns = [
    path('home/',homePage,name='home'),
    path('liststudent/',StudentListView.as_view(),name='student_list'),
    path('getstudent/<int:pk>',StudentDetailView.as_view(),name='student_details'),
    path('addstudent/',StudentCreateView.as_view(),name='createstudent'),
    #path('createstudent/',createStudent,name='createstudent')
]
