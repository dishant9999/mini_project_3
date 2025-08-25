# timetable/models.py
from django.db import models
from users.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Stream(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    semester = models.IntegerField()
    division = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} - Sem {self.semester} Div {self.division}"

class Professor(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    short_form = models.CharField(max_length=10)
    subjects = models.ManyToManyField('Subject', blank=True)
    streams = models.ManyToManyField(Stream, blank=True)
    weekly_lecture_hours = models.IntegerField()
    punch_in_time = models.TimeField(null=True, blank=True)
    punch_out_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    semester = models.IntegerField()
    division = models.CharField(max_length=10)
    professors = models.ManyToManyField(Professor, blank=True)
    lecture_duration = models.DurationField()
    lectures_per_week = models.IntegerField()

    def __str__(self):
        return self.name

class Timetable(models.Model):
    days_per_week = models.IntegerField()
    shift_start_time = models.TimeField()
    shift_end_time = models.TimeField()
    number_of_lectures = models.IntegerField()

    def __str__(self):
        return f"Timetable: {self.days_per_week} days, {self.number_of_lectures} lectures"

# timetable/models.py (add after existing models)

class Lesson(models.Model):
    day_choices = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
    ]
    day = models.CharField(max_length=3, choices=day_choices)
    start_time = models.TimeField()
    end_time = models.TimeField()
    number = models.PositiveSmallIntegerField()  # Period number in day
    
    def __str__(self):
        return f"{self.get_day_display()} Lesson {self.number} ({self.start_time}-{self.end_time})"

class LectureSlot(models.Model):
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    location = models.ForeignKey('location.Location', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.stream} {self.lesson} {self.subject} by {self.professor}"
