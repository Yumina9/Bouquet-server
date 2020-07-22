from rest_framework import serializers
from flowers.models import Flower

class FlowerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    flower_name= serializers.CharField(max_length=100)
    flower_mean =serializers.CharField(max_length=100)
    flower_season = serializers.CharField(max_length=20)
    flower_color = serializers.CharField(max_length=10)

    def create(self, validated_data):
        return Flower.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.flower_name = validated_data.get('flower_name', instance.flower_name)
        instance.flower_mean = validated_data.get('flower_mean', instance.flower_mean)
        instance.flower_season = validated_data.get('flower_season', instance.flower_season)
        instance.flower_color = validated_data.get('flower_color', instance.flower_color)
        instance.save()
        return instance