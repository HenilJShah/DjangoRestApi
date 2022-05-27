from django.urls import path
from .views import StudentCreate, StudentDestroy, StudentList, StudentListCreate, StudentListCreateCRUD, StudentRetrieve, StudentRetrieveUpdate, StudentRetrieveUpdateDestroy, StudentRetrieveUpdateDestroyCRUD, StudentUpdate

urlpatterns = [
    path('ls/', StudentList.as_view()),
    path('add/', StudentCreate.as_view()),
    path('search/<int:pk>/', StudentRetrieve.as_view()),
    path('upd/<int:pk>/', StudentUpdate.as_view()),
    path('del/<int:pk>/', StudentDestroy.as_view()),
    path('ls_or_add/', StudentListCreate.as_view()),
    path('ls_or_upd/<int:pk>/', StudentRetrieveUpdate.as_view()),
    path('ls_or_upd_or_del/<int:pk>/', StudentRetrieveUpdateDestroy.as_view()),

    # crud
    path('crud/', StudentListCreateCRUD.as_view()),
    path('crud/<int:pk>/', StudentRetrieveUpdateDestroyCRUD.as_view()),
]