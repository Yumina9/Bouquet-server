from rest_framework import serializers
from flowers.models import Flower
from shops.serializers import ShopSerializer

class FlowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flower
        fields = '__all__'
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        print(instance)
        print(response) 
        response['shops'] = FlowerSerializer(instance.shops).data
        return response