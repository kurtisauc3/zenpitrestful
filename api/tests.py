from django.test import TestCase
from .models import DeviceList

class ModelTestCase(TestCase):
    """Here lie the tests for DeviceList, may they suceed in their endeavors"""

    def setup_device(self):
        """Tryna make a phone with a bunch of stuff, yep..."""
        self.device_name = "The Bond Phone"
        self.battery_status = "100"
        self.longitude = "51.509865"
        self.latitude = "-0.118092"
        self.devicelist = DeviceList(device_name=self.device_name, battery_status=self.battery_status, longitude=self.longitude, latitude=self.latitude)

    def save_device(self):
        """Makin sure we can save phones to the database."""
        old_count = DeviceList.objects.count()
        self.devicelist.save()
        new_count = DeviceList.objects.count()
        self.assertNotEqual(old_count, new_count)
