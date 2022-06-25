from rest_framework.routers import DefaultRouter

from SerializerRelationsApi.views import SingerViewSet, SongsViewSet

router = DefaultRouter()

router.register("singer", SingerViewSet, basename="sin")
router.register("song", SongsViewSet, basename="song")

urlpatterns = router.urls
