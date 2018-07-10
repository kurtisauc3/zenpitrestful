from rest_framework import generics
from .serializers import DeviceSerializer
from .models import Device

class CreateView(generics.ListCreateAPIView):
    """A class that handles what the creating a device page looks like."""
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    # override for the serializer perform_create function
    def perform_create(self, serializer):
        """Save data when creating a device."""
        serializer.save()

class DetailsView(generics.RetrieveAPIView):
    """A class that handles what the looking at a device looks like."""

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
