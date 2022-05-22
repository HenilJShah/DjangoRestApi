from django.urls import path

from .views import CrudStudentValidation

urlpatterns = [
    path('validate/', CrudStudentValidation.as_view()),
]