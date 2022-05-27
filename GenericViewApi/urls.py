from django.urls import path
from .views import StudentApi, StudentCreate, StudentDelete, StudentRetrieve, StudentUpdate, List_and_Create_Student, update_retrieve_and_delete_student
urlpatterns = [
    path('fetch/', StudentApi.as_view()),
    path('create/', StudentCreate.as_view()),
    path('update/<int:pk>/', StudentUpdate.as_view()),
    path('search/<int:pk>/', StudentRetrieve.as_view()),
    path('delete/<int:pk>/', StudentDelete.as_view()),

    # group work
    path('stu/', List_and_Create_Student.as_view()),
    path('stu/<int:pk>/', update_retrieve_and_delete_student.as_view())
]
