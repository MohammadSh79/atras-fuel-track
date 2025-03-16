from django.db import models
from DigitalSign.models import DigitalSign
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

class User(PermissionsMixin, AbstractBaseUser):
    username = models.TextField(unique=True, blank=True, null=True)
    union_name = models.ForeignKey('Union.Union', on_delete=models.CASCADE, related_name='members', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD =  'username'
    
    class Meta:
        permissions = [
            ("is_union", "Whether this account is for a union or not"),
        ]

class RealUser(User):
    first_name = models.TextField()
    last_name = models.TextField()
    certificate_id = models.TextField()
    national_code = models.TextField(unique=True)
    father_name = models.TextField()
    birth_date = models.DateField()
    phone_number = models.TextField()

    USERNAME_FIELD = 'national_code'

class LegalUser(User):
    company_name = models.TextField()
    representative_name = models.TextField()
    national_id = models.TextField(unique=True)
    economy_number = models.TextField()
    registered_number = models.TextField()

    USERNAME_FIELD = 'national_id'

class CoownerUser(RealUser):
    digital_sign = models.OneToOneField(DigitalSign, on_delete=models.CASCADE, related_name="owner", null=True)

class MachineOwner(RealUser):
    pass