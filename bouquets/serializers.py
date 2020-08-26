from rest_framework import serializers

from bouquets.models import Bouquet
from shops.serializers import ShopSerializer


class BouquetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bouquet
        fields='__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        print(instance)
        print(response) 
        response['shops'] = ShopSerializer(instance.shops).data
        return response
