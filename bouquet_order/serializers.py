from rest_framework import serializers
from bouquet_order.models import Bouquet_order
from shops.models import Shop
from bouquets.models import Bouquet
from flowers.models import Flower

class BouquetOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bouquet_order
        fields = '__all__'

    def create(self, validated_data):
        return Bouquet_order.objects.create(**validated_data)
