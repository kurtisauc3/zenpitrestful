from django.test import TestCase
from .models import DeviceList
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ModelTestCase(TestCase):
    """Here lie the tests for DeviceList models, may they suceed in their endeavors"""

    def setup_device(self):
        """Tryna make a phone with a bunch of stuff, yep..."""
        self.device_id = "007TBP"
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

class ViewTestCase(TestCase):
    """Here lie the tests for DeviceList views, may they suceed in their endeavors"""

    def setup_device(self):
        """Set up client and some mock data."""
        self.client = APIClient()
        self.devicelist_data = {'device_name': 'The Bond Phone'}
        self.response = self.client.post(
            reverse('create'),
            self.devicelist_data,
            format="json")

    def create_device(self):
        """Compare it to the http status code."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
