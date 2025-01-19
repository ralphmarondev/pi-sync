from django.db import models


class TestPerson(models.Model):
    name = models.CharField(max_length=50)
    is_deleted = models.BooleanField(default=False)
    data_created = models.DateTimeField(auto_now_add=True)
