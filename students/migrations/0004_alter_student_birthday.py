# Generated by Django 3.2.4 on 2021-07-03 23:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
