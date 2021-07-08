from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render # noqa
from django.views.decorators.csrf import csrf_exempt

from faker import Faker

from students.forms import StudentCreateForm, StudentUpdateForm
from students.models import Student
from students.utils import format_list, format_records

from webargs import fields, validate
from webargs.djangoparser import use_args, use_kwargs


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
        if param_value:
            students = students.filter(**{param_name: param_value})

    html_form = """
        <form method="get">

        <label for="fname">First name:</label>
        <input type="text" name="first_name"><br><br>

        <label for="lname">Last name:</label>
        <input type="text" name="last_name"><br><br>

        <label>Age:</label>
        <input type="number" name="age"><br><br>

        <input type="submit" value="Search">

       </form>
    """

    records = format_records(students)

    response = html_form + records

    return HttpResponse(response)


@csrf_exempt
def create_student(request):

    if request.method == 'GET':

        form = StudentCreateForm()

    elif request.method == 'POST':

        form = StudentCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students')

    html_form = f"""
                <form method="post">
                {form.as_p()}
                <input type="submit" value="Create">
                </form>
                """

    response = html_form

    return HttpResponse(response)


@csrf_exempt
def update_student(request, id): # noqa

    student = Student.objects.get(id=id)

    if request.method == 'GET':

        form = StudentUpdateForm(instance=student)

    elif request.method == 'POST':

        form = StudentUpdateForm(
            instance=student,
            data=request.POST
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students')

    html_form = f"""
                <form method="post">
                {form.as_p()}
                <input type="submit" value="Save">
                </form>
                """

    response = html_form

    return HttpResponse(response)
