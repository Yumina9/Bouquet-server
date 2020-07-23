from rest_framework import serializers
from shops.models import Shop

class ShopSerializer(serializers.Serializer):
    shop_id = serializers.IntegerField(read_only=True)
    shop_name = serializers.CharField(max_length=200)
    shop_location = serializers.CharField(max_length=200)
    shop_florist = serializers.CharField(max_length=50)
    shop_description = serializers.CharField(max_length=300)
    shop_phone = serializers.CharField(max_length=50)
    shop_instagram = serializers.CharField(max_length=100)
    shop_facebook = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Shop.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.shop_id = validated_data.get('shop_id', instance.shop_id)
        instance.shop_name = validated_data.get('shop_name', instance.shop_name)
        instance.shop_location = validated_data.get('shop_location', instance.shop_location)
        instance.shop_florist = validated_data.get('shop_florist', instance.shop_florist)
        instance.shop_description = validated_data.get('shop_description', instance.shop_description)
        instance.shop_phone = validated_data.get('shop_phone', instance.shop_phone)
        instance.shop_instagram = validated_data.get('shop_instagram', instance.shop_instagram)
        instance.shop_facebook = validated_data.get('shop_facebook', instance.shop_facebook)        
        instance.save()
        return instance