from rest_framework import serializers
from .models import Device

class DeviceSerializer(serializers.ModelSerializer):
    """Serializer that makes our models funky fresh JSON."""

    class Meta:
        """Meta class to synch up models to serializer."""
        model = Device
        fields = (
            'id',
            'device_name',
            'battery_status',
            'longitude',
            'latitude',
            'timestamp',
        )
        read_only_fields = ('timestamp',)
