from django.db import models

class Location(models.Model):
    ROOM_TYPES = [
        ('Room', 'Room'),
        ('Lab', 'Lab'),
        ('Auditorium', 'Auditorium'),
    ]

    room_number = models.CharField(max_length=20, unique=True)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)

    def __str__(self):
        return f"{self.room_type} - {self.room_number}"
