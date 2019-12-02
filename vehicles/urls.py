from rest_framework.routers import SimpleRouter
from django.urls import path, include
from vehicles.views import location

from vehicles.viewsets import (LocationViewSet, VehicleCoordsViewSet,
                               VehicleViewSet, vehicle_detail)

router = SimpleRouter()
router.register('locations', LocationViewSet)
router.register('vehicle-locations', VehicleCoordsViewSet)
router.register('vehicles', VehicleViewSet)
# router.register('vehicle-detail', VehicleDetailViewSet)

urlpatterns = [
    # path('', get_location),
    path('coord/', location),
    path('vehicle-detail/<int:pk>', vehicle_detail),
    path('', include(router.urls)),
]
