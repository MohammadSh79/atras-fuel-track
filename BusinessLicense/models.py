from django.db import models
from User.models import MachineOwner

class BusinessLicenseImage(models.Model):
    image = models.ImageField(upload_to="business_licenses/")
    owner = models.ForeignKey(MachineOwner, on_delete=models.CASCADE, related_name="business_licenses")