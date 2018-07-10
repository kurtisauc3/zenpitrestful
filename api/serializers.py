from rest_framework import serializers
from .models import DeviceList

class DeviceListSerializer(serializers.ModelSerializer):
    """Serializer that makes our models funky fresh JSON."""

    class Meta:
        """Meta class to synch up models to serializer."""
        model = DeviceList
        fields = ('device_id', 'device_name', 'battery_status', 'longitude', 'latitude', 'timestamp')
        read_only_fields = ('timestamp',)
        lookup_field = ('device_id')
