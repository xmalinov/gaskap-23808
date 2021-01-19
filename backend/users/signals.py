from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string

from .models import School, Student


@receiver(post_save, sender=School)
def on_school_saved(sender, instance, created, **kwargs):
    if created:
        if not instance.student_code:
            instance.student_code = "S" + str(instance.id) + get_random_string(length=4)
        if not instance.teacher_code:
            instance.teacher_code = "T" + str(instance.id) + get_random_string(length=4)
        instance.save()


@receiver(post_save, sender=Student)
def on_student_saved(sender, instance, created, **kwargs):
    if created:
        if not instance.student_id:
            instance.student_id = str(instance.id) + get_random_string(length=4)
        instance.save()
