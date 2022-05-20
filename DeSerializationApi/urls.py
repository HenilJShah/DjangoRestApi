from django.urls import path

from .views import CreateData

urlpatterns = [
    path('stucreate/', CreateData, name='student_create'),   
]