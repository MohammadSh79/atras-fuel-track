from django.db import models
from User.models import MachineOwner
from django.contrib import admin

class BusinessLicenseImage(models.Model):
    image = models.ImageField(upload_to="business_licenses/")
    owner = models.ForeignKey(MachineOwner, on_delete=models.CASCADE, related_name="business_licenses")

admin.site.register(BusinessLicenseImage)