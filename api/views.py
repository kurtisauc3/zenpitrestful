from rest_framework import generics
from .serializers import DeviceListSerializer
from .models import DeviceList

class CreateView(generics.ListCreateAPIView):
    """A class that handles what the creating a device page looks like."""
    queryset = DeviceList.objects.all()
    serializer_class = DeviceListSerializer

    def perform_create(self, serializer):
        """Save data when creating a device."""
        serializer.save()

class DetailsView(generics.RetrieveAPIView):
    """A class that handles what the looking at a device looks like."""

    queryset = DeviceList.objects.all()
    serializer_class = DeviceListSerializer
