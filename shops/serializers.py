from rest_framework import serializers
from shops.models import Shop
from bouquets.serializers import BouquetSerializer
from bouquets.models import Bouquet
from flowers.models import Flower
from flowers.serializers import FlowerSerializer


class ShopSerializer(serializers.ModelSerializer):

    bouquets = serializers.SerializerMethodField(
        source='bouquet_set', read_only=True)

    flowers = serializers.SerializerMethodField(
        source='flower_set', read_only=True)

    class Meta:
        model=Shop
        fields = '__all__'


    def get_bouquets(self, obj):
        query = Bouquet.objects.filter(shops__id=obj.id)[:3]
        serializer = BouquetSerializer(query, many=True)
        return serializer.data

    def get_flowers(self, obj):
        query = Flower.objects.filter(shops__id=obj.id)[:3]
        serializer = FlowerSerializer(query, many=True)
        return serializer.data
