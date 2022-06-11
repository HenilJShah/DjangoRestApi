from django.urls import path
from rest_framework.routers import DefaultRouter

from ViewSetApi.views import StudentApi

router = DefaultRouter()

router.register('crud', StudentApi, basename='api')


urlpatterns = router.urls