from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    hint_password = models.CharField(max_length=200, blank=True, null=True)
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=200, blank=True, null=True, default='Admin')
    is_deleted = models.BooleanField(default=False)
    update_date = models.DateTimeField(auto_now=True)
    registered_doors = models.ManyToManyField('rooms.Door', related_name='users', blank=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username
