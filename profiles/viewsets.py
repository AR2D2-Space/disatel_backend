from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

from profiles.models import Profile
from profiles.serializers import ProfileSerializer, ProfileDetailSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'last_name', 'email', 'username', 'dpi']

    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Profile.objects.all()
        else:
            return Profile.objects.filter(is_superuser=False, pk=user.id)

    def get_serializer_class(self):
        user = self.request.user
        if user.is_superuser:
            return ProfileSerializer
        else:
            return ProfileDetailSerializer
