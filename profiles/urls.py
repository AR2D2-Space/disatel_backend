from rest_framework.routers import SimpleRouter


from profiles.viewsets import ProfileViewSet

router = SimpleRouter()
router.register('profiles', ProfileViewSet)

urlpatterns = router.urls
