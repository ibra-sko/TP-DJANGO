from rest_framework import serializers
from concession_api.models import Concession, Vehicule

class ConcessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concession
        fields = ['id', 'nom', 'code_postal', 'adresse']  # numero_siret exclu


class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = '__all__'