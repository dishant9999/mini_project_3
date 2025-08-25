from django.core.management.base import BaseCommand
from timetable.models import Timetable, Lesson
import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning)

class Command(BaseCommand):
    help = 'Create Lesson objects for each Timetable based on number_of_lectures'

    def handle(self, *args, **kwargs):
        for timetable in Timetable.objects.all():
            for i in range(1, timetable.number_of_lectures + 1):
                lesson, created = Lesson.objects.get_or_create(timetable=timetable, number=i)
                if created:
                    self.stdout.write(f"Created Lesson {i} for Timetable {timetable.id}")
                else:
                    self.stdout.write(f"Lesson {i} for Timetable {timetable.id} already exists")

