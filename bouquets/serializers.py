from rest_framework import serializers
from bouquets.models import Bouquet
from flowers.serializers import FlowerSerializer
from ribbons.serializers import RibbonSerializer
from wrappingPapers.serializers import WrappingPaperSerializer

class BouquetSerializer(serializers.ModelSerializer):

    flower = FlowerSerializer(many=True, read_only=True)
    ribbon = RibbonSerializer(many=True, read_only=True)
    wrappingPaper = WrappingPaperSerializer(many=True, read_only=True)
    class Meta:
        model=Bouquet
        fields='__all__'