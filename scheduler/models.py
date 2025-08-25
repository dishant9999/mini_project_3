from django.db import models
from users.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    priority = models.IntegerField()
    expected_duration = models.DurationField()
    date = models.DateField()
    scheduled_start_time = models.TimeField(null=True, blank=True)
    scheduled_end_time = models.TimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    pending = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} (User: {self.user.username})"

class FreeTimeSlot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Free time for {self.user.username} on {self.date} from {self.start_time} to {self.end_time}"
