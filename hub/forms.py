from django import forms
from .models import Student

class StudentForm(forms.Form):
    first_name=forms.CharField(label='first name', max_length=50, required=False)
    last_name=forms.CharField(label='last name', max_length=50, required=False)
    email=forms.EmailField()

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__' # ['last_name',...]
        #exclude = []