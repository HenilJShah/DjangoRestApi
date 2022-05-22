from django.urls import path
from .views import CrudStudent

urlpatterns = [
    path('db/', CrudStudent.as_view()),   
]