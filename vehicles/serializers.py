from rest_framework.serializers import ModelSerializer

from vehicles.models import (Vehicle, Location)


class LocationSerializer(ModelSerializer):
    def create(self, validated_data):
        location = Location.objects.create(**validated_data)
        return location

    class Meta:
        model = Location
        exclude = ['vehicle']


class VehicleCoordsSerializer(ModelSerializer):
    locations = LocationSerializer(many=True)

    class Meta:
        model = Vehicle
        fields = ['id', 'model', 'registration_number', 'locations']

    def create(self, validated_data):
        locations_data = validated_data.pop('locations')
        vehicle = Vehicle.objects.create(**validated_data)
        for location_data in locations_data:
            Location.objects.create(vehicle=vehicle, **location_data)
        return vehicle


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'identifier', 'registration_number']

    def create(self, validated_data):
        vehicle = Vehicle.objects.create(**validated_data)
        return vehicle


class VehicleDetailSerializer(ModelSerializer):
    def create(self, validated_data):
        vehicle = Vehicle.objects.create(**validated_data)
        return vehicle

    class Meta:
        model = Vehicle
        exclude = ['fleet', 'created']

