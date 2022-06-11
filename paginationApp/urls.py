from rest_framework.routers import DefaultRouter

from paginationApp.views import StudentPaginationsClass

router = DefaultRouter()
router.register("data", StudentPaginationsClass, basename="api")

urlpatterns = router.urls
