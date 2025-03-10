from django.db import models

class DigitalSign(models.Model):
    image = models.ImageField(upload_to='DigitalSigns/')