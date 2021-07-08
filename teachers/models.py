import random

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker


# Create your models here.

# Homework 7
class Teacher(models.Model):
    first_name = models.CharField(max_length=50, null=False, validators=[
        MinLengthValidator(2)
    ])
    last_name = models.CharField(max_length=80, null=False, validators=[
        MinLengthValidator(3)
    ])
    phone_number = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=120, null=True)
    experience = models.IntegerField(default=5, null=False)

# Homework 8
    def __str__(self):
        return f'{self.first_name}, {self.last_name }, {self.phone_number}, {self.email}, {self.experience}'

    @staticmethod
    def generate_teachers(count):
        faker = Faker()
        for _ in range(count):
            tc = Teacher(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                experience=random.randint(3, 10),
            )

            tc.save()
