from django.forms import DateInput, ModelForm

import django_filters

from groups.models import Group


class GroupBaseForm(ModelForm):
    class Meta:
        model = Group
        fields = ['group_name',
                  'lessons_total',
                  'start_date',
                  'end_date',
                  ]
        widgets = {
                      'start_date': DateInput(attrs={'type': 'date'}),
                      'end_date': DateInput(attrs={'type': 'date'}),
        }

    @staticmethod
    def normalize_name(value):
        return value.lower().capitalize()

    def clean_group_name(self):
        group_name = self.cleaned_data['group_name']
        result = self.normalize_name(group_name)
        return result


class GroupCreateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        fields = '__all__'
        exclude = ['end_date']


class GroupUpdateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        fields = '__all__'


# Homework 13
class GroupsFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = {
            'group_name': ['exact', 'icontains'],
            'lessons_total': ['lt', 'gt'],
        }
