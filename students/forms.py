import re

from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelForm

import django_filters

from students.models import Student


class StudentBaseForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'age',
            'phone_number',
            'birthday',
            'group',
            'enroll_date',
            'graduate_date',
        ]
        # fields = '__all__'
        widgets = {
            'birthday': DateInput(attrs={'type': 'date'}),
            'enroll_date': DateInput(attrs={'type': 'date'}),
            'graduate_date': DateInput(attrs={'type': 'date'}),
        }

    @staticmethod
    def normalize_name(value):
        return value.lower().capitalize()

    @staticmethod
    def normalize_phone_number(value):
        return '+' + re.sub('\D', '', value) # noqa

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        result = self.normalize_name(first_name)
        return result

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        result = self.normalize_name(last_name)
        return result

    # def clean_birthday(self):
    #     birthday = self.cleaned_data['birthday']
    #     age = datetime.datetime.now().year - birthday.year
    #     if age < 18:
    #         raise ValidationError('Age should be greater than 18 y.o.')
    #
    #     return birthday

    def clean(self):
        enroll_date = self.cleaned_data['enroll_date']
        graduate_date = self.cleaned_data['graduate_date']
        if enroll_date > graduate_date:
            raise ValidationError('Enroll date coudnt be greater than graduate date!')

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        result = self.normalize_phone_number(phone_number)
        return result


class StudentCreateForm(StudentBaseForm):
    pass


class StudentUpdateForm(StudentBaseForm):
    class Meta(StudentBaseForm.Meta):
        # fields = [
        #    'first_name',
        #   'last_name',
        #    # 'age',
        #    'phone_number',
        #    'birthday',
        #    'enroll_date',
        #    'graduate_date',
        # ]
        fields = '__all__'


class StudentsFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'age': ['lt', 'gt'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }
