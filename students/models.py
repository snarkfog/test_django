import datetime

from core.models import Person

from dateutil.relativedelta import relativedelta # noqa
from django.core.validators import MinLengthValidator # noqa
from django.db import models

from faker import Faker # noqa

from groups.models import Group

from students.validators import AdultValidator # noqa


# Create your models here.
class Student(Person):
    # first_name = models.CharField(max_length=50, null=False, validators=[
    #     MinLengthValidator(2)
    # ])
    # last_name = models.CharField(max_length=80, null=False)
    # age = models.IntegerField(default=42, null=False)
    # phone_number = models.CharField(max_length=15, unique=True, null=True)
    # email = models.EmailField(max_length=120, null=True)
    # birthday = models.DateField(default=datetime.date.today, null=True,
    #                             validators=[AdultValidator(21)]
    #                             )
    enroll_date = models.DateField(default=datetime.date.today, null=True)
    graduate_date = models.DateField(default=datetime.date.today, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')

    def __str__(self):
        return f'{self.full_name()}, ' \
               f'{self.age}, ' \
               f'{self.phone_number}, ' \
               f'{self.email} ' \
               f'{self.birthday}, ' \
               f'{self.group}' \
               f'{self.enroll_date},' \
               f'{self.graduate_date}'

    # def full_name(self):
    #     return f'{self.first_name}, {self.last_name}'

    # @staticmethod
    # def generate_students(count):
    #     faker = Faker()
    #     for _ in range(count):
    #         st = Student(
    #             first_name=faker.first_name(),
    #             last_name=faker.last_name(),
    #             email=faker.email(),
    #             birthday=faker.date_between(start_date='-65y', end_date='-18y'),
    #         )
    #
    #         st.age = relativedelta(datetime.date.today(), st.birthday).years
    #         st.save()

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        obj.save()
