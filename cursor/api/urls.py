from django.urls import path
from . views import StudentList

urlpatterns = [
    path('studentapi/', StudentList.as_view()),
]
