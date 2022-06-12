from rest_framework import serializers
from StudentApp.models import Student, School, Book

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        
        fields = (
            'student_id',
            'first_name',
            'last_name',
            'email',
            'gender',
            'school_id',
            'books_id'
        )


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        
        fields = (
            'school_id'
            'region'
            'school_name',
            'email',
            'principal_name',
            'phone',
            'address'
        )


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        
        fields = (
            'book_id'
            'title',
            'author_name',
            'date_of_publication',
            'number_pages',
        )
