from django.db import models

class DeviceList(models.Model):
    """This class is the device list model."""
    device_name = models.CharField(max_length=255, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Nice readablility."""
        return "{}".format(self.name)
