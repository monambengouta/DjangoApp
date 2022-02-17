from wsgiref.util import request_uri
from django.http import HttpResponse
from django.shortcuts import render
from hub.models import Coach, Student

# Create your views here.
def homePage(request):
    return HttpResponse("<h1> Welcome To the home page !</h1>")

def student_details(request,id):
    student=Student.objects.get(id=id)
    return render(
        request,
        'hub/st_details.html',
        {
            'student':student,
        }
    )

def student_list(request):
    list=Student.objects.all()
    list_coachs=Coach.objects.all()
    
    return render(
        request,
        'hub/index.html',
        {
            'students':list,
            'coachs':list_coachs,
        }
    )