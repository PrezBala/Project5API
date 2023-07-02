from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import (
    MovieViewSet,
    RatingViewSet,
    UserViewSet,
    CustomAuthToken,
)

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('movies', MovieViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
]
