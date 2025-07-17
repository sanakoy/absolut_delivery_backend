from django.urls import path, include
from rest_framework.routers import DefaultRouter

from delivery_absolute.views.package_type import PackageTypeViewSet
from delivery_absolute.views.service_type import ServiceTypeViewSet
from delivery_absolute.views.staus import StatusViewSet
from delivery_absolute.views.transport_model import TransportModelViewSet
from .views.delivery import DeliveryViewSet

router = DefaultRouter()
router.register(r'deliveries', DeliveryViewSet, basename='delivery')
router.register(r'service-type', ServiceTypeViewSet, basename='service-type')
router.register(r'package-type', PackageTypeViewSet, basename='package-type')
router.register(r'transport-model', TransportModelViewSet, basename='transport-model')
router.register(r'status', StatusViewSet, basename='status')

urlpatterns = [
    path('', include(router.urls)),
]