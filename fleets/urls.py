from rest_framework.routers import SimpleRouter

from fleets.viewsets import FleetViewSet, FleetDetailViewSet

router = SimpleRouter()
router.register('fleets', FleetViewSet)
router.register('fleet-detail', FleetDetailViewSet)

urlpatterns = router.urls
