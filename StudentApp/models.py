from pyexpat import model
from django.db import models
from django.forms import NullBooleanField

# Create your models here.


class School(models.Model):
    school_id = models.AutoField(primary_key=True, auto_created=True)
    region = models.IntegerField()
    school_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)
    principal_name = models.CharField(max_length=80, null=True)
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)


class Book(models.Model):
    book_id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=50)
    author_name = models.CharField(max_length=80, null=True)
    date_of_publication = models.DateField(null=True)
    number_pages = models.IntegerField(null=True)


class Student(models.Model): 
    student_id = models.AutoField(primary_key=True, auto_created=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True)
    email = models .CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10, null=True)
    school_id = models.IntegerField(null = True)
    books_id = models.IntegerField(null = True)
    # school_id = models.ForeignKey(School, on_delete=models.SET_NULL, blank=True, null=True)    
    # books_id = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
     


