from django.db import models


# Create your models here.
class Group(models.Model):
    group_name = models.CharField(max_length=50, null=False)
    course_name = models.CharField(max_length=80, null=False)
    lessons_total = models.IntegerField(default=30)
    students_quantity = models.IntegerField(default=15)
