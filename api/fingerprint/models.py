from django.db import models

class FingerprintTemplate(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, unique=True)
    template = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name if self.name else "Unnamed Template"