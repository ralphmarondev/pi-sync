from django.db import models

class History(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey('rooms.Door', on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.room.name} - {self.description} by {self.username} at {self.timestamp}'
