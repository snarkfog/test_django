from courses.models import Course

from django.forms import DateInput, ModelForm

import django_filters


class CourseCreateForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'})
        }


class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = {
            'name': ['exact', 'icontains'],
            'start_date': ['lt', 'gt'],
            'end_date': ['lt', 'gt'],
        }
