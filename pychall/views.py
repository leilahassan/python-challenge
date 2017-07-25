from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from.models import datetime
#from.models import Workers

# Create your views here.
#def welcome(request):
    #return render(request,'welcome_workers.html')
#def Workers(request):
    #return HttpResponse("<p>welcome to our workers page</p>")

#def welcome(request):
    #return render(request,'welcome_students.html')
#def students(request):
    #student = Student.objects.get(id=2)
    #return HttpResponse(student.course)
    
def welcome(request):
    return render(request,'welcome_students.html')
def students(request):
    student = Student.objects.all()
    context = {
            'student':student
        }
    return render(request,'listing_students.html',context) 
     
