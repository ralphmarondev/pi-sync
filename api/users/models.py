import os
from uuid import uuid4

from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    hint_password = models.CharField(max_length=200, blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=200, default='Admin')
    is_deleted = models.BooleanField(default=False)
    update_date = models.DateTimeField(auto_now=True)
    registered_doors = models.ManyToManyField('rooms.Door', related_name='users', blank=True)

    image = models.CharField(max_length=200, blank=True, null=True)  # we will store path as string
    fingerprint_template = models.CharField(max_length=200, blank=True, null=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username

    def save_fingerprint(self, template):
        self.fingerprint_template = template
        self.save()

    def get_fingerprint(self):
        return self.fingerprint_template

    def save_image(self, uploaded_file):
        if uploaded_file:
            root_folder = os.path.join(os.getcwd(), "user_images")
            os.makedirs(root_folder, exist_ok=True)  # Create folder if it doesn't exist

            file_extension = os.path.splitext(uploaded_file.name)[1]
            unique_filename = f'user_{self.id}_{uuid4().hex}{file_extension}'
            file_path = os.path.join(root_folder, unique_filename)

            with open(file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            # Store relative path in database
            self.image = f'user_images/{unique_filename}'
            self.save()
    def get_image_url(self):
        if self.image:
            return f'{settings.MEDIA_URL}{self.image}'
        return None