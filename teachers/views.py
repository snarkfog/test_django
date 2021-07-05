from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render # noqa
from django.views.decorators.csrf import csrf_exempt

from teachers.forms import TeacherCreateForm
from teachers.models import Teacher
from teachers.utils import format_records

from webargs import fields
from webargs.djangoparser import use_args

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
        if param_value:
            teachers = teachers.filter(**{param_name: param_value})

    html_form = """
        <form method="get">

        <label for="fname">First name:</label>
        <input type="text" name="first_name"><br><br>

        <label for="lname">Last name:</label>
        <input type="text" name="last_name"><br><br>

        <label>Experience:</label>
        <input type="number" name="experience"><br><br>

        <input type="submit" value="Submit">

       </form>
        """

    records = format_records(teachers)

    response = html_form + records

    return HttpResponse(response)


# Homework 8
@csrf_exempt
def create_teacher(request):

    if request.method == 'GET':

        form = TeacherCreateForm()

    elif request.method == 'POST':

        form = TeacherCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers')

    html_form = f"""
                <form method="post">
                {form.as_p()}
                <input type="submit" value="Submit">
                </form>
                """

    response = html_form

    return HttpResponse(response)
