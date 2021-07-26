import re

from django.forms import ModelForm

import django_filters

from teachers.models import Teacher


class TeacherBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'experience'
        ]

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

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        result = self.normalize_phone_number(phone_number)
        return result


class TeacherCreateForm(TeacherBaseForm):
    pass


class TeacherUpdateForm(TeacherBaseForm):
    class Meta(TeacherBaseForm.Meta):
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            # 'experience',
        ]


# Homework 13
class TeachersFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'experience': ['lt', 'gt'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }
