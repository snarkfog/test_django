from django.contrib import admin

from students.models import Student

from .models import Group


class StudentsInlineTable(admin.TabularInline):
    model = Student
    fields = [
        'last_name',
        'first_name',
        'email',
        'age',
    ]

    # readonly_fields = fields
    # show_change_link = True             # edit in Student model

    extra = 0               # default = 3


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'group_name',
        'start_date',
        'end_date',
        'headman',
    ]

    fields = [
        'name',
        ('start_date', 'end_date'),
        'headman',
        'teachers',
    ]

    inlines = [StudentsInlineTable]


admin.site.register(Group, GroupAdmin)
