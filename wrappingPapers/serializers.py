from rest_framework import serializers
from wrappingPapers.models import WrappingPaper

class WrappingPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = WrappingPaper
        fields = '__all__'
