import datetime

from dateutil.relativedelta import relativedelta

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from core.validators import AdultValidator # noqa


# Create your models here.
class Person(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=50, validators=[
        MinLengthValidator(2)
    ])
    last_name = models.CharField(max_length=80)
    age = models.IntegerField(default=42)
    phone_number = models.CharField(max_length=15, unique=True, null=True)
    email = models.EmailField(max_length=120, null=True)
    birthday = models.DateField(default=datetime.date.today,
                                # validators=[AdultValidator(18)]
                                )

    def __str__(self):
        return f'{self.full_name()}, {self.birthday}'

    def full_name(self):
        return f'{self.first_name}, {self.last_name}'

    def save(self, *args, **kwargs):
        self.age = relativedelta(datetime.date.today(), self.birthday).years
        super().save(*args, **kwargs)

    @classmethod
    def _generate(cls):
        faker = Faker()
        st = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            birthday=faker.date_between(start_date='-65y', end_date='-18y'),
        )

        st.age = relativedelta(datetime.date.today(), st.birthday).years
        st.save()
        return st

    @classmethod
    def generate(cls, count):
        for _ in range(count):
            cls._generate()
