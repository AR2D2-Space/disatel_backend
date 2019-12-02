from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from fleets.models import Fleet
from fleets.serializers import FleetSerializer, FleetDetailSerializer


class FleetViewSet(ModelViewSet):
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'type', 'country']

    def get_queryset(self):
        user = self.request.user
        return Fleet.objects.filter(profile=user)


class FleetDetailViewSet(ModelViewSet):
    queryset = Fleet.objects.all()
    serializer_class = FleetDetailSerializer
