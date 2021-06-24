# from django.shortcuts import render
from django.http import HttpResponse
from webargs.djangoparser import use_kwargs
from webargs import fields, validate
from faker import Faker
from html_formatters import format_list


# Create your views here.
def hello(request):
    return HttpResponse('Hello')


# Lesson 07 Homework. Generate fake students function
@use_kwargs({
    "count": fields.Int(
        required=False,
        missing=10,
        validate=[validate.Range(min=1, max=100)]
    )
},
    location="query"
)
def generate_students(request, count):
    fake_students = Faker(["uk_UA"])
    return HttpResponse(format_list(fake_students.name() for _ in range(count)))
