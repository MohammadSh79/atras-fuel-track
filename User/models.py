from django.db import models
from DigitalSign.models import DigitalSign
from django.contrib.auth.models import AbstractBaseUser
from django.contrib import admin

class User(AbstractBaseUser):
    class Meta:
        abstract = True

class RealUser(User):
    first_name = models.TextField()
    last_name = models.TextField()
    certificate_id = models.TextField()
    national_code = models.TextField()
    father_name = models.TextField()
    birth_date = models.DateField()
    phone_number = models.TextField()

    USERNAME_FIELD = 'national_code'

class LegalUser(User):
    company_name = models.TextField()
    representative_name = models.TextField()
    national_id = models.TextField()
    economy_number = models.TextField()
    registered_number = models.TextField()

    USERNAME_FIELD = 'national_id'

class CoownerUser(RealUser):
    digital_sign = models.OneToOneField(DigitalSign, on_delete=models.CASCADE, related_name="owner")

class MachineOwner(RealUser):
    pass

admin.site.register(RealUser)
admin.site.register(LegalUser)
admin.site.register(CoownerUser)
admin.site.register(MachineOwner)