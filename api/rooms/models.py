from django.db import models

class Door(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_open = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=200, default="Admin")
    is_deleted = models.BooleanField(default=False)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        state = 'Open' if self.is_open else 'Closed'
        return f'{self.name} - {state}'
