from django.urls import path
from .views import CrudModel

urlpatterns = [
    path('crud/', CrudModel.as_view()),
]