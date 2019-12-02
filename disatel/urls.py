from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import (obtain_jwt_token, refresh_jwt_token,
                                      verify_jwt_token)

urlpatterns = [
    path('root/', admin.site.urls),
    path('api/', include('profiles.urls')),
    path('api/', include('fleets.urls')),
    path('api/', include('vehicles.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
]
