from django.urls import path
from .views import ClassBasedCRUDApi

urlpatterns = [
    path('api/', ClassBasedCRUDApi.as_view()),
]