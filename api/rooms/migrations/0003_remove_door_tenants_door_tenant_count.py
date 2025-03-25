# Generated by Django 5.1.2 on 2025-03-25 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_door_tenants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='door',
            name='tenants',
        ),
        migrations.AddField(
            model_name='door',
            name='tenant_count',
            field=models.IntegerField(default=0),
        ),
    ]
