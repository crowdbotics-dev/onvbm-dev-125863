from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Hcsde2ViewSet, Hcsde2ViewSet, Hcsde2ViewSet, Hcsde2ViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("hcsde2", Hcsde2ViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
