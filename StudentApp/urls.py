from django.urls import path, re_path
from StudentApp import views

urlpatterns = [
    path('students/', views.SearchStudents),
    re_path(r'^students/([0-9]+)$', views.getStudent),
    path('students/add', views.addStudent),
]