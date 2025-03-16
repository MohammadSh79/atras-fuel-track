from django.db import models
from User.models import CoownerUser
from Machine.models import Machine
from User.models import User

class Union(User):
    title = models.TextField()

    organization_choices = (
        ("VEZARAT_SAMT", "وزارت صنعت معدن و تجارت"),
        ("VEZARAT_JAHAD", "سازمان جهاد کشاورزی"),
    )

    organization = models.TextField(choices=organization_choices)