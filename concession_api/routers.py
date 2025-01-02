from rest_framework_nested.routers import DefaultRouter, NestedSimpleRouter
from .views import ConcessionViewSet, VehiculeViewSet

# main router
router = DefaultRouter()
router.register(r'concessions', ConcessionViewSet, basename='concession')

# nested router
concession_router = NestedSimpleRouter(router, r'concessions', lookup='concession')
concession_router.register(r'vehicules', VehiculeViewSet, basename='concession-vehicules')
