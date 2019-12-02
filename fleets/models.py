from django.db.models import (Model, CharField, IntegerField,
                              ForeignKey, CASCADE, DateTimeField)

from profiles.models import Profile


class Fleet(Model):
    COUNTRY_CHOICES = [
        ('GT', 'Guatemala'),
        ('ELS', 'El Salvador')
    ]
    TYPE_CHOICES = [
        ('Lg', 'Trailer'),
        ('Md', 'Camiones'),
        ('Sm', 'Automoviles')
    ]
    name = CharField(max_length=30)
    identifier = IntegerField()
    country = CharField(max_length=5, choices=COUNTRY_CHOICES)
    profile = ForeignKey(Profile, related_name='fleets', on_delete=CASCADE)
    type = CharField(max_length=2, choices=TYPE_CHOICES)
    created = DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}-{self.identifier} ({self.profile})'
