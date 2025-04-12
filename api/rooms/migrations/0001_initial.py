# Generated by Django 5.1.2 on 2025-04-12 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_open', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(default='Admin', max_length=200)),
                ('is_deleted', models.BooleanField(default=False)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('tenant_count', models.IntegerField(default=0)),
            ],
        ),
    ]
