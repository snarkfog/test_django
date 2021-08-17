from django.contrib import admin

from groups.models import Group

from students.models import Student


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
        'group_name',
        ('start_date', 'end_date'),
        'headman',
        'teachers',
    ]

    search_fields = ['group_name', 'start_date']

    inlines = [StudentsInlineTable]


admin.site.register(Group, GroupAdmin)
