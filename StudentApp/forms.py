from django import forms

from StudentApp.models import *


class NewStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'gender', 'school_id', 'books_id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        school_choices = [(o.school_id, o.school_name) for o in School.objects.all()]
        book_choices =  [(o.book_id, o.title) for o in Book.objects.all()]

        # self.fields['student_id'] = forms.IntegerField(label="ID")
        self.fields['first_name'] = forms.CharField(label="First Name", max_length=30)
        self.fields['last_name'] = forms.CharField(label="Last Name", max_length=30)
        self.fields['email'] = forms.CharField(label="Email", max_length=100)
        self.fields['gender'] = forms.CharField(label="Gender", max_length=10)
        
        self.fields['school_id'] = forms.ChoiceField(choices = school_choices)
        self.fields['books_id'] = forms.ChoiceField(choices = book_choices)
        
class SearchStudentForm(forms.Form):
    class Meta:
        fields = ['student_id', 'student_name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['student_id'] = forms.IntegerField(label="Student Id")
        self.fields['student_name'] = forms.CharField(label="Student Name", max_length=60)

