from unicodedata import name
from django.urls import path
from .views import homePage ,student_list,student_details,StudentListView,StudentDetailView

urlpatterns = [
    path('home/',homePage,name='home'),
    path('liststudent/',StudentListView.as_view(),name='student_list'),
    path('getstudent/<int:pk>',StudentDetailView.as_view(),name='student_details'),
]
