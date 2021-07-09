from django.forms import DateInput, ModelForm

from groups.models import Group


class GroupBaseForm(ModelForm):
    class Meta:
        model = Group
        fields = ['group_name',
                  'lessons_total',
                  'start_date',
                  ]
        widgets = {
                      'start_date': DateInput(attrs={'type': 'date'}),
        }

    @staticmethod
    def normalize_name(value):
        return value.lower().capitalize()

    def clean_group_name(self):
        group_name = self.cleaned_data['group_name']
        result = self.normalize_name(group_name)
        return result


class GroupCreateForm(GroupBaseForm):
    pass


class GroupUpdateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        fields = [
            'group_name',
            # 'lessons_total',
            'start_date',
        ]
