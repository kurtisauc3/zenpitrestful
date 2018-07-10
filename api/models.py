from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

'''
    Our model for our devices, which stores:
    device_name: Required, max 255,
    battery_status: Between 0 and 100, defaults to 0
    longitude/latitude: defaults to 0.000000
    timestamp: automatically added, cannot edit
'''
class Device(models.Model):
    """This class is the device list model."""
    #device_id = models.CharField(max_length=32, unique=True, null=False)
    device_name = models.CharField(max_length=255, blank=False,)
    battery_status = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ],
    )
    longitude = models.DecimalField(
        default=0.000000,
        max_digits=9,
        decimal_places=6,
    )
    latitude = models.DecimalField(
        default=0.000000,
        max_digits=9, decimal_places=6,
    )
    timestamp = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        """Nice readablility."""
        return "{}".format(self.device_name)
