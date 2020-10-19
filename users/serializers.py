from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'user_choice', 'user_phone', 'zip_code', 'user_address', 'shop',)
        # fields = "__all__"

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    user_choice = serializers.CharField(max_length=1)
    user_phone = serializers.CharField(max_length=13)
    zip_code = serializers.CharField(max_length=5)
    user_address = serializers.CharField(max_length=200)
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'user_choice', 'user_phone', 'zip_code', 'user_address')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
