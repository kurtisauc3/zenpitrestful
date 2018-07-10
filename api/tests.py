from django.test import TestCase
from .models import DeviceList
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ModelTestCase(TestCase):
    """Here lie the tests for DeviceList models, may they suceed in their endeavors"""

    def setUp(self):
        """Tryna make a phone with a bunch of stuff, yep..."""
        self.device_id = "007TBP"
        self.device_name = "The Bond Phone"
        self.battery_status = "100"
        self.longitude = "51.509865"
        self.latitude = "-0.118092"
        self.devicelist = DeviceList(device_id=self.device_id, device_name=self.device_name, battery_status=self.battery_status, longitude=self.longitude, latitude=self.latitude)

    def test_save_device(self):
        """Makin sure we can save phones to the database."""
        old_count = DeviceList.objects.count()
        self.devicelist.save()
        new_count = DeviceList.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Here lie the tests for DeviceList views, may they suceed in their endeavors"""

    def setUp(self):
        """Set up client and some mock data."""
        self.device_id = "007TBP"
        self.device_name = "The Bond Phone"
        self.battery_status = "100"
        self.longitude = "51.509865"
        self.latitude = "-0.118092"
        self.client = APIClient()
        self.devicelist_data = {'device_id': '007TBP', 'device_name': 'The Bond Phone', 'battery_status': '100', 'longitude': '51.509865', 'latitude': '-0.118092'}
        self.response = self.client.post(
            reverse('create'),
            self.devicelist_data,
            format="json")

    def test_create_device(self):
        """Compare it to the http status code."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_device(self):
        """Check that you can get devices by device id."""
        devicelist = DeviceList.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': devicelist.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, devicelist)
