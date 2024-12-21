from rest_framework import serializers
from base.models.vendor import VendorItems

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorItems
        fields = '__all__'
        read_only_fields = ['user', 'status'] 