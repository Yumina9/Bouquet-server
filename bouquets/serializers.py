from rest_framework import serializers
from bouquets.models import Bouquet
from flowers.serializers import FlowerSerializer

class BouquetSerializer(serializers.ModelSerializer):

    flower = FlowerSerializer(many=True, read_only=True)
    class Meta:
        model=Bouquet
        fields='__all__'

