from django.db import models
from User.models import MachineOwner
from django.contrib import admin

class Machine(models.Model):
    registered_number = models.IntegerField()
    engine_number = models.IntegerField()
    chassis_number = models.IntegerField()
    cylinder_count = models.IntegerField()
    number_plate = models.TextField()

    general_type_choices = (
        ("RAHSAZI", "راه سازی"),
        ("KESHAVARZI", "کشاورزی")
    )

    general_type = models.TextField(choices=general_type_choices)

    general_sub_type_choices = (
        ("LOADER", "لودر"),
        ("BILMECHANIKI", "بیل مکانیکی"),
        ("BOLDOUZER", "بلدوزر"),
        ("GRADER", "گریدر"),
        ("BOBCAT", "باب کت"),
        ("TRACTOR", "تراکتور"),
    )

    general_sub_type = models.TextField(choices=general_sub_type_choices)

    model_choices = (
        ("LOADER950", "950 لودر"),
    )

    model = models.TextField(choices=model_choices)
    owner = models.ForeignKey(MachineOwner, on_delete=models.CASCADE, related_name="machines")

admin.site.register(Machine)