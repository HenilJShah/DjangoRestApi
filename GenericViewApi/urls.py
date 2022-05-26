from django.urls import path
from .views import StudentApi, StudentCreate, StudentRetrieve, StudentUpdate
urlpatterns = [
    path('fetch/', StudentApi.as_view()),
    path('create/', StudentCreate.as_view()),
    path('update/<int:pk>/', StudentUpdate.as_view()),
    path('search/<int:pk>', StudentRetrieve.as_view()),
]
