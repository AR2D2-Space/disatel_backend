from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from threading import Event

from vehicles.models import Vehicle, Location
from vehicles.serializers import LocationSerializer


# def set_interval(func, time):
#     e = Event()
#     while not e.wait(time):
#         func()
#
# def get_location():
#     url = 'https://api.wheretheiss.at/v1/satellites/25544'
#     response = requests.get(url)
#     r = response.json()
#     identifier = r['id']
#     lat = r['latitude']
#     long = r['longitude']
#     velocity = r['velocity']
#     print(velocity, 'YA ESTAS OBTENIENDO LA DATA DE UBICACION!!!!!!')
#
#     vehicle = Vehicle.objects.get(identifier=identifier)
#     new_location = Location(
#         vehicle=vehicle,
#         lat=lat,
#         long=long,
#         velocity=velocity
#     )
#     new_location.save()
#     locationes = Location.objects.all()
#     serializers = LocationSerializer(locationes, many=True)
#     return Response(serializers.data, status=status.HTTP_201_CREATED)
#
#
# set_interval(get_location, 1)


@api_view(['GET'])
def location(request):
    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)
