from django.db import models
from django.contrib import admin

class DigitalSign(models.Model):
    image = models.ImageField(upload_to='DigitalSigns/')

admin.site.register(DigitalSign)