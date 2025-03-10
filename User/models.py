from django.db import models
from DigitalSign.models import DigitalSign

class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    certificate_id = models.IntegerField()
    national_code = models.IntegerField()
    father_name = models.TextField()
    birth_date = models.DateField()
    phone_number = models.TextField()

class PassAuthUser(User):
    password = models.TextField()

class CoownerUser(PassAuthUser):
    digital_sign = models.OneToOneField(DigitalSign, on_delete=models.CASCADE, related_name="owner")

class MachineOwner(User):
    pass