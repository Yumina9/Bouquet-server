from rest_framework import serializers
from shops.models import Shop
from bouquets.models import Bouquet
from flowers.models import Flower
from ribbons.models import Ribbon
from wrappingPapers.models import WrappingPaper
from bouquet_order.models import Bouquet_order

from bouquets.serializers import BouquetSerializer
from flowers.serializers import FlowerSerializer
from ribbons.serializers import RibbonSerializer
from wrappingPapers.serializers import WrappingPaperSerializer
from bouquet_order.serializers import BouquetOrderSerializer

class ShopSerializer(serializers.ModelSerializer):

    bouquets = serializers.SerializerMethodField(
        source='bouquet_set', read_only=True)

    flowers = serializers.SerializerMethodField(
        source='flower_set', read_only=True)

    ribbons = serializers.SerializerMethodField(
        source='ribbon_set', read_only=True
    )

    wrappingPapers = serializers.SerializerMethodField(
        source='wrappingPaper_set', read_only=True
    )

    bouquet_order = serializers.SerializerMethodField(
        source='bouquet_order_set', read_only=True
    )

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

    def get_ribbons(self, obj):
        query = Ribbon.objects.filter(shops__id=obj.id)[:3]
        serializer = RibbonSerializer(query, many=True)
        return serializer.data

    def get_wrappingPapers(self, obj):
        query= WrappingPaper.objects.filter(shops__id=obj.id)[:3]
        serializer = WrappingPaperSerializer(query, many=True)
        return serializer.data

    def get_bouquet_order(self, obj):
        query= Bouquet_order.objects.select_related('bouquet').select_related('flower').filter(shops__id=obj.id)
        serializer = BouquetOrderSerializer(query, many=True)
        return serializer.data