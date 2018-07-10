from rest_framework import serializers
from .models import DeviceList

class DeviceListSerializer(serializers.ModelSerializer):
    """Serializer that makes our models funky fresh JSON."""

    class Meta:
        """Meta class to synch up models to serializer."""
        model = DeviceList
        fields = ('id', 'device_name', 'timestamp', 'battery_status', 'longitude', 'latitude')
        read_only_fields = ('timestamp',)
