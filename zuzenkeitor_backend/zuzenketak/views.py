from django.http import HttpResponse
from django.shortcuts import render

from zuzenketak.models import Exercise, Student

# Create your views here.
def index(request):
    return render(request, "index.html",context={})

def exercices(request):
    context ={'exercises': Exercise.objects.all()}
    return render(request, "exercises.html", context=context)

def exercice(request, exercice_id):
    context ={'exercice': Exercise.objects.get(id=exercice_id)}
    return render(request, "exercise.html", context=context)

def students(request):
    context ={'students': Student.objects.all()}
    return render(request, "students.html", context=context)

def student(request, student_id):
    context ={'student': Student.objects.ge(id=student_id)}
    return render(request, "student.html", context=context)

