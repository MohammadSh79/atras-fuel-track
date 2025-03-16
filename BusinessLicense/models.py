from django.db import models
from User.models import User

class BusinessLicenseImage(models.Model):
    image = models.ImageField(upload_to="business_licenses/")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="business_licenses")