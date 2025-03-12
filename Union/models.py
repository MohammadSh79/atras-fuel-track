from django.db import models
from User.models import CoownerUser
from Machine.models import Machine
from django.contrib import admin

class Union(models.Model):
    title = models.TextField()

    organization_choices = (
        ("VEZARAT_SAMT", "وزارت صنعت معدن و تجارت"),
        ("VEZARAT_JAHAD", "وزارت جهاد کشاورزی"),
    )

    organization = models.TextField(choices=organization_choices)
    coowner = models.OneToOneField(CoownerUser, on_delete=models.CASCADE, related_name="union")
    machines = models.ForeignKey(Machine, on_delete=models.CASCADE)

admin.site.register(Union)