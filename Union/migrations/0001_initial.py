# Generated by Django 5.1.7 on 2025-03-12 12:36

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Machine', '0001_initial'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Union',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('title', models.TextField()),
                ('organization', models.TextField(choices=[('VEZARAT_SAMT', 'وزارت صنعت معدن و تجارت'), ('VEZARAT_JAHAD', 'سازمان جهاد کشاورزی')])),
                ('machines', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Machine.machine')),
            ],
            options={
                'abstract': False,
            },
            bases=('User.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
