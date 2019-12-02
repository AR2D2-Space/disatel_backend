from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.http import HttpResponse

from fleets.models import Fleet
from vehicles.models import Vehicle


class FleetSerializer(ModelSerializer):
    vehicles = SerializerMethodField('get_vehicles')

    def get_vehicles(self, profile):
        fleets = Fleet.objects.filter(pk=profile.id)
        fleet_ids = [x.id for x in fleets]
        count_vehicles = Vehicle.objects.filter(fleet_id__in=fleet_ids).count()
        return count_vehicles

    class Meta:
        model = Fleet
        fields = ['id', 'name', 'identifier',  'type', 'country', 'vehicles']

    def create(self, validated_data):
        vehicles_data = validated_data.pop('vehicles')
        fleet = Fleet.objects.create(**validated_data)
        for vehicle_data in vehicles_data:
            if vehicle_data.type == fleet.type:
                Vehicle.objects.create(fleet=fleet, **vehicle_data)
            else:
                return HttpResponse('Error, tipo de vehiculo erroneo segun la flota seleccionada.')
        return fleet


class FleetDetailSerializer(ModelSerializer):
    class Meta:
        model = Fleet
        exclude = ['id', 'profile', 'created']

    def create(self, validated_data):
        fleet = Fleet.objects.create(**validated_data)
        return fleet
