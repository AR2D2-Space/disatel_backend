from django.db.models import (Model, CharField, IntegerField,
                              ForeignKey, CASCADE, DateTimeField,
                              DateField, TimeField, FloatField,
                              SmallIntegerField)

from fleets.models import Fleet


class Vehicle(Model):
    TYPE_CHOICES = [
        ('Lg', 'Trailer'),
        ('Md', 'Camion'),
        ('Sm', 'Automovil')
    ]
    identifier = IntegerField()
    fleet = ForeignKey(Fleet, related_name='vehicles', on_delete=CASCADE)
    brand = CharField(max_length=30)
    model = IntegerField()
    type = CharField(max_length=20, choices=TYPE_CHOICES)
    color = CharField(max_length=30)
    registration_number = CharField(max_length=8)
    created = DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.identifier} - {self.fleet}'


class Location(Model):
    vehicle = ForeignKey(Vehicle, related_name='locations', on_delete=CASCADE)
    date = DateField(auto_now=True)
    hour = TimeField(auto_now=True)
    lat = FloatField()
    long = FloatField()
    direction = CharField(max_length=50, null=True, blank=True)
    velocity = FloatField()

    def __str__(self):
        return f'{self.vehicle}-({self.lat}, {self.long})'


class Event(Model):
    start = SmallIntegerField(default=0)
    down = SmallIntegerField(default=0)
    date = DateField(auto_now=True)
    hour = TimeField(auto_now=True)
    lat = CharField(max_length=25)
    long = CharField(max_length=25)
    direction = CharField(max_length=50)

    def __str__(self):
        return f'{self.start}-{self.down}'
