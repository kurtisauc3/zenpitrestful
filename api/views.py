from rest_framework import generics
from .serializers import DeviceListSerializer
from .models import DeviceList

class CreateView(generics.ListCreateAPIView):
    """A class that handles what the creating a device page looks like."""
    queryset = DeviceList.objects.all()
    serializer_class = DeviceListSerializer

    def create_it(self, serializer):
        """Save data when creating a device."""
        serializer.save()
