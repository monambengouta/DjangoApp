from turtle import update
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.shortcuts import render,redirect
from django.urls import reverse
from hub.forms import StudentForm, StudentModelForm
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
    template_name="hub/index.html" #default student_list.html
    context_object_name="students" #defaults: object_list
    #paginate_by= 5
    
class StudentDetailView(DetailView):
    model=Student
    template_name="hub/st_details.html"

def createStudent(request):
    form=StudentForm()
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
            return redirect('student_list')
            
    # if request.method =='POST' and request.POST.get('email').endswith('@esprit.tn'):
    #     firstName=request.POST.get('first_name')
    #     lastName=request.POST.get('last_name')
    #     email=request.POST.get('email')
    #     Student.objects.create(
    #         first_name=firstName,
    #         last_name=lastName,
    #         email=email
    #     )
    #     return redirect('student_list')
    return render(
    request,
    'hub/add_student.html',
    {
        'form':form
    }
    )
    
def addStudentForm(request):
    form = StudentModelForm
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid:
            student = form.save(commit=False)
            student.save()
            return redirect('student_list')
    return render(
    request,
    'hub/add_student.html',
    {
        'form':form
    }
    )        

class StudentCreateView(CreateView):
    model=Student
    form_class=StudentModelForm
    def get_success_url(self):
        return reverse("student_list")

class StudentUpdateView(UpdateView):
    pass