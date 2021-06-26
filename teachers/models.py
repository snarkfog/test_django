from django.db import models
from faker import Faker
import random


# Create your models here.

# Homework 7
class Teacher(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=80, null=False)
    email = models.EmailField(max_length=120, null=True)
    experience = models.IntegerField(default=5, null=False)

# Homework 8
    def __str__(self):
        return f'{self.first_name}, {self.last_name }, {self.email}, {self.experience}'

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
