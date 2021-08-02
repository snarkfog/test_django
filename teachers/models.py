from random import randint

from core.models import Person

from django.core.validators import MinLengthValidator # noqa
from django.db import models

from faker import Faker # noqa

from groups.models import Group


# Create your models here.

# Homework 7
class Teacher(Person):
    # first_name = models.CharField(max_length=50, null=False, validators=[
    #     MinLengthValidator(2)
    # ])
    # last_name = models.CharField(max_length=80, null=False, validators=[
    #     MinLengthValidator(3)
    # ])
    # phone_number = models.CharField(max_length=15, unique=True, null=True)
    # email = models.EmailField(max_length=120, null=True)
    experience = models.IntegerField(default=5)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='teachers')

# Homework 8
    def __str__(self):
        return f'{self.first_name}, ' \
               f'{self.last_name }, ' \
               f'{self.group}, ' \
               f'{self.phone_number}, ' \
               f'{self.email}, ' \
               f'{self.experience}'

    # @staticmethod
    # def generate_teachers(count):
    #     faker = Faker()
    #     for _ in range(count):
    #         tc = Teacher(
    #             first_name=faker.first_name(),
    #             last_name=faker.last_name(),
    #             email=faker.email(),
    #             experience=random.randint(3, 10),
    #         )
    #
    #         tc.save()

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        obj.experience = randint(1, 10)
        obj.save()
