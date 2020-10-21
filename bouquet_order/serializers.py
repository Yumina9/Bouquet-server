from rest_framework import serializers
from bouquet_order.models import Bouquet_order
from shops.models import Shop
from bouquets.models import Bouquet
from flowers.models import Flower
from bouquets.serializers import BouquetSerializer
from flowers.serializers import FlowerSerializer

class BouquetOrderSerializer(serializers.ModelSerializer):

    bouquet = serializers.SerializerMethodField(
        source='bouquet', read_only=True)

    flower = serializers.SerializerMethodField(
        source='flower', read_only=True)


    class Meta:
        model = Bouquet_order
        fields = '__all__'

    def create(self, validated_data):
        return Bouquet_order.objects.create(**validated_data)

    def get_bouquet(self, obj):
        serializer = BouquetSerializer(obj.bouquet)
        return serializer.data

    def get_flower(self, obj):
        serializer = FlowerSerializer(obj.flower)
        return serializer.data