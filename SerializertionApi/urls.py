from django.urls import path
from .views import student_detail, student_detail_all

urlpatterns = [
    path('stuinfo/<int:id>', student_detail, name='stuinfo'),
    path('stuinfo/', student_detail_all, name='stuinfo'),
]