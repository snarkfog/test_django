import datetime

from django.core.exceptions import ValidationError


def adult_validator(birthday):
    ADULT_AGE_LIMIT = 18 # noqa

    age = datetime.datetime.now().year - birthday.year
    if age < ADULT_AGE_LIMIT:
        raise ValidationError('Age should be greater than 18 y.o.')
