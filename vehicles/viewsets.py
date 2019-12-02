from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from vehicles.models import Vehicle, Location
from vehicles.serializers import (LocationSerializer, VehicleCoordsSerializer,
                                  VehicleSerializer, VehicleDetailSerializer)
from fleets.models import Fleet


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class VehicleCoordsViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleCoordsSerializer


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [SearchFilter]
    search_fields = ['brand', 'model', 'type', 'color', 'registration_number', 'fleet__id']

    def get_queryset(self):
        user = self.request.user
        fleet = Fleet.objects.get(pk=user.id)
        return Vehicle.objects.filter(fleet__id=fleet.id)


# class VehicleDetailViewSet(ModelViewSet):
#     queryset = Vehicle.objects.all()
#     serializer_class = VehicleDetailSerializer
#

@csrf_exempt
def vehicle_detail(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    if request.method == 'GET':
        try:
            serializer = VehicleSerializer(vehicle)
            print(serializer.data)
            return JsonResponse(serializer.data)
        except Vehicle.DoesNotExist:
            return HttpResponse('No enviaste un solicitante con valor valido.')
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VehicleSerializer(vehicle, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
