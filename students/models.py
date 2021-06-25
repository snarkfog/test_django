from django.db import models
import datetime
from faker import Faker


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=80, null=False)
    age = models.IntegerField(default=42)
    email = models.EmailField(max_length=120, null=True)
    birthday = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.full_name()}, {self.birthday}'

    def full_name(self):
        return f'{self.first_name}, {self.last_name}'

    @staticmethod
    def generate_students(count):
        faker = Faker()
        for _ in range(count):
            st = Student(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                birthday=faker.date_between(start_date='-65y', end_date='-18y')
            )

            st.save()
