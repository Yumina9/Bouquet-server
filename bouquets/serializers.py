from rest_framework import serializers
from bouquets.models import Bouquet

class BouquetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bouquet
        fields='__all__'