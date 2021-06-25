# from django.shortcuts import render
from django.http import HttpResponse
from webargs.djangoparser import use_kwargs, use_args
from webargs import fields, validate
from faker import Faker
from students.utils import format_list, format_records
from students.models import Student


# Create your views here.
def hello(request):
    return HttpResponse('Hello')


# Lesson 07 Homework. Generate fake students function
@use_kwargs({
    'count': fields.Int(
        required=False,
        missing=10,
        validate=[validate.Range(min=1, max=100)]
    )
},
    location='query'
)
def generate_students(request, count):
    fake_students = Faker(['uk_UA'])
    return HttpResponse(format_list(fake_students.name() for _ in range(count)))


@use_args({
    'first_name': fields.Str(
        required=False,
    ),
    'last_name': fields.Str(
        required=False,
    ),
    'birthday': fields.Date(
        required=False,
    )
},
    location='query'
)
def get_students(request, args):
    students = Student.objects.all()

    for param_name, param_value in args.items():
        students = students.filter(**{param_name: param_value})

    records = format_records(students)
    return HttpResponse(records)
