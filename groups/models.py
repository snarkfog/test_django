import datetime
import random

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker


# Create your models here.

# Homework 7
class Group(models.Model):
    group_name = models.CharField(max_length=30, null=False, validators=[
        MinLengthValidator(2)
    ])
    lessons_total = models.IntegerField(default=30, null=False)
    start_date = models.DateField(default=datetime.date.today(), null=False)
    end_date = models.DateField(null=True, blank=True)
    headman = models.OneToOneField(
        'students.Student',
        on_delete=models.SET_NULL,
        null=True,
        related_name='headed_group'
    )

    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

# Homework 8
    def __str__(self):
        return f'{self.group_name}, {self.lessons_total}, {self.start_date}'

    @staticmethod
    def generate_groups(count):
        faker = Faker()
        for _ in range(count):
            gr = Group(
                group_name=faker.first_name(),
                lessons_total=random.randint(15, 30),
                start_date=datetime.date.today()
            )

            gr.save()
