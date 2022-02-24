
from pyexpat import model
from django.views.generic import ListView,DetailView
from django.http import HttpResponse
from django.shortcuts import render
from hub.models import Coach, Student

# Create your views here.
def homePage(request):
    return render(
        request,
        'base.html'
    )
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
class StudentListView(ListView):
    model=Student
    template_name="hub/index.html"
    paginate_by= 5
    
class StudentDetailView(DetailView):
    model=Student
    template_name="hub/st_details.html"