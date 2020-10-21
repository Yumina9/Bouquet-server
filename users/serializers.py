from rest_framework import serializers
from users.models import User
from bouquet_order.models import Bouquet_order
from bouquet_order.serializers import BouquetOrderSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'user_choice', 'user_phone', 'shop','bouquet_order')
        # fields = "__all__"

    bouquet_order = serializers.SerializerMethodField(source='bouquet_order_set', read_only=True)

    def get_bouquet_order(self, obj):
        query= Bouquet_order.objects.filter(shops__id=obj.id)[:5]
        serializer = BouquetOrderSerializer(query, many=True)
        return serializer.data

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    # user_id = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    user_choice = serializers.CharField(max_length=1)
    user_phone = serializers.CharField(max_length=13)
    
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'user_choice', 'user_phone')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
