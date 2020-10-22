from rest_framework import serializers
from flowers.models import Flower

class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = ['name', 'description', 'season', 'color', 'price', 'img']
