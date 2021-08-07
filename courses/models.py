import datetime

from django.db import models

from groups.models import Group # noqa


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(null=True, blank=True)
    group = models.OneToOneField(
        'groups.Group',
        on_delete=models.SET_NULL,
        null=True,
        related_name='courses'
    )

    def __str__(self):
        return self.name
