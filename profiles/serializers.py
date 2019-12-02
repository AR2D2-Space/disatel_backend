from rest_framework.serializers import ModelSerializer, SerializerMethodField

from profiles.models import Profile
from fleets.models import Fleet


class ProfileSerializer(ModelSerializer):
    fleets = SerializerMethodField('get_fleets')

    def get_fleets(self, profile):
        count_fleets = Fleet.objects.filter(profile=profile).count()
        return count_fleets

    def create(self, validated_data):
        instance = Profile.objects.create_user(**validated_data)
        return instance

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('frist_name', instance.first_name)
    #     instance.code = validated_data.get('last_name', instance.last_name)
    #     instance.linenos = validated_data.get('username', instance.username)
    #     instance.language = validated_data.get('email', instance.email)
    #     instance.style = validated_data.get('dpi', instance.dpi)
    #     instance.style = validated_data.get('password', instance.password)
    #     instance.save()
    #     return instance

    class Meta:
        model = Profile
        fields = ['id', 'username', 'fleets', 'dpi', 'last_login']


class ProfileDetailSerializer(ModelSerializer):

    class Meta:
        model = Profile
        exclude = ['created', 'last_login']
