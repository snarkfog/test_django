# from django.shortcuts import render
from webargs.djangoparser import use_args
from webargs import fields
from teachers.models import Teacher
from django.http import HttpResponse
from teachers.utils import format_records


# Create your views here.


# Homework 8
@use_args({
    'first_name': fields.Str(
        required=False,
    ),
    'last_name': fields.Str(
        required=False,
    ),
    'email': fields.Email(
        required=False,
    ),
    'experience': fields.Int(
        required=False,
    )
},
    location='query'
)
def get_teachers(request, args):
    teachers = Teacher.objects.all()

    for param_name, param_value in args.items():
        teachers = teachers.filter(**{param_name: param_value})

    records = format_records(teachers)
    return HttpResponse(records)
