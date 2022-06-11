from django.urls import path

from filteringApp.views import StudentList, StudentSeach, StudentOrdering

urlpatterns = [
    path('', StudentList.as_view()),
    path('se/', StudentSeach.as_view()),
    path('or/', StudentOrdering.as_view()),
]
