# Generated by Django 5.1.7 on 2025-03-12 07:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessLicenseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='business_licenses/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_licenses', to='User.machineowner')),
            ],
        ),
    ]
