from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Stream(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()
    division = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.name} - Sem {self.semester} Div {self.division}"

class Professor(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    short_form = models.CharField(max_length=10)
    subjects = models.ManyToManyField('Subject', blank=True)
    streams = models.ManyToManyField(Stream, blank=True)
    weekly_lecture_hours = models.PositiveIntegerField(default=0)
    punch_in_time = models.TimeField(null=True, blank=True)
    punch_out_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    semester = models.PositiveIntegerField()
    division = models.CharField(max_length=1)
    professors = models.ManyToManyField(Professor, blank=True)
    lecture_duration = models.DurationField()
    lectures_per_week = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Location(models.Model):
    room_number = models.CharField(max_length=20)
    room_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.room_number} - {self.room_type}"

class Timetable(models.Model):
    days_per_week = models.PositiveIntegerField()
    shift_start_time = models.TimeField()
    shift_end_time = models.TimeField()
    number_of_lectures = models.PositiveIntegerField()

class Lesson(models.Model):
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()

class LectureSlot(models.Model):
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
class Timetable(models.Model):
    days_per_week = models.PositiveIntegerField(default=5)
    shift_start_time = models.TimeField()
    shift_end_time = models.TimeField()
    number_of_lectures = models.PositiveIntegerField(default=8)

    def __str__(self):
        return f"Timetable (Days: {self.days_per_week}, Lectures: {self.number_of_lectures})"

class Lesson(models.Model):
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()

    def __str__(self):
        return f"Lesson {self.number}"

class LectureSlot(models.Model):
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    stream = models.ForeignKey('Stream', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    day = models.PositiveIntegerField()  # 0=Monday, ...

    class Meta:
        unique_together = [('timetable', 'stream', 'day', 'lesson')]

    def __str__(self):
        return f"{self.stream} - {self.subject} on Day {self.day}, Lesson {self.lesson.number}"
