from re import S
import re
from tkinter.tix import CheckList
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse



from StudentApp.models import Student, School, Book
from StudentApp.serializers import StudentSerializer, SchoolSerializer, BookSerializer
from StudentApp.forms import *
# Create your views here.

@csrf_exempt
def SearchStudents(request):
    
    form = SearchStudentForm()
    if request.method == 'POST':
        form = SearchStudentForm(request.POST)
        if form.is_valid():
            try:
                    
                student_data = Student.objects.get(student_id = form.data.get('student_id'))
                full_name = '{} {}'.format(student_data.first_name, student_data.last_name)

                if (not full_name.startswith(form.data.get('student_name'))):
                    return JsonResponse({500: "Id and name does not match"})
                
                requested_data = {
                    'FullName': full_name,
                    'StudentEmail': student_data.email,
                    'Gender': student_data.gender,
                    'SchoolName': School.objects.get(school_id = student_data.school_id).school_name,
                    'SchoolPhone': School.objects.get(school_id = student_data.school_id).phone,
                    'BooksRead': Book.objects.get(book_id = student_data.books_id).title,
                    'TotalPagesRead': Book.objects.get(book_id = student_data.books_id).number_pages,
                }
                return JsonResponse(requested_data)
            except: 
                return JsonResponse({500: "Failed - no such student"})

    return render(request, 'search.html', {'form': form})

@csrf_exempt
def getStudent(request, id):
    # print('id=', id)
    try:
        student_data = Student.objects.get(student_id = id)
        # student_serialized = StudentSerializer(student_data)

        #(Student Full Name, Student Email, Gender, School Name, School Phone, Books read by that student, Total number of book pages read by the student)
        full_name = '{} {}'.format(student_data.first_name, student_data.last_name)
        requested_data = {
            'FullName': full_name,
            'StudentEmail': student_data.email,
            'Gender': student_data.gender,
            'SchoolName': School.objects.get(school_id = student_data.school_id).school_name,
            'SchoolPhone': School.objects.get(school_id = student_data.school_id).phone,
            'BooksRead': Book.objects.get(book_id = student_data.books_id).title,
            'TotalPagesRead': Book.objects.get(book_id = student_data.books_id).number_pages,
        }
        
        return JsonResponse(requested_data, safe=False)

    except:
        return JsonResponse({500: "Failed - no such student"})


@csrf_exempt
def addStudent(request):
    form = NewStudentForm()
    if request.method == 'POST':
        form = NewStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({201: "created"})

    return render(request, 'add.html',  {'form': form})
