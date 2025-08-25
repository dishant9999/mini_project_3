def generate_timetable(timetable, streams, subjects, professors, locations):
    from .models import Lesson, LectureSlot

    LectureSlot.objects.filter(timetable=timetable).delete()

    lessons = list(Lesson.objects.filter(timetable=timetable).order_by('number'))
    num_days = timetable.days_per_week

    day = 0
    lesson_idx = 0

    for stream in streams:
        stream_subjects = subjects.filter(stream=stream)

        for subject in stream_subjects:
            professor = subject.professors.first()
            location = locations.first()

            if not professor or not location:
                continue

            les = lessons[lesson_idx % len(lessons)]

            lec_slot = LectureSlot(
                timetable=timetable,
                lesson=les,
                stream=stream,
                subject=subject,
                professor=professor,
                location=location,
                day=day
            )
            lec_slot.save()

            lesson_idx += 1
            if lesson_idx % len(lessons) == 0:
                day = (day + 1) % num_days

    return True
