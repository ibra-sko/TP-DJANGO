from rest_framework import viewsets

from concession_api.models import Concession, Vehicule
from concession_api.serializers import ConcessionSerializer, VehiculeSerializer


class ConcessionViewSet(viewsets.ModelViewSet):
    queryset = Concession.objects.all()
    serializer_class = ConcessionSerializer


class VehiculeViewSet(viewsets.ModelViewSet):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer

    def get_queryset(self):
        # Récupérer l'ID de la concession depuis l'URL
        concession_id = self.kwargs.get('concession_pk')
        # Retourner uniquement les véhicules liés à cette concession
        return Vehicule.objects.filter(concession_id=concession_id)
