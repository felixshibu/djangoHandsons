from rest_framework import serializers
from .models import InventoryModel

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryModel
        fields = '__all__'