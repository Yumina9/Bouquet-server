from rest_framework import serializers
from ribbons.models import Ribbon


class RibbonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ribbon
        fields = '__all__'
