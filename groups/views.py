from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render # noqa
from django.views.decorators.csrf import csrf_exempt

from groups.forms import GroupCreateForm
from groups.models import Group
from groups.utils import format_records

from webargs import fields
from webargs.djangoparser import use_args
# Create your views here.


# Homework 8
@use_args({
    'group_name': fields.Str(
        required=False,
    ),
    'lessons_total': fields.Int(
        required=False,
    ),
    'start_date': fields.Date(
        required=False,
    )
},
    location='query'
)
def get_groups(request, args):
    groups = Group.objects.all()

    for param_name, param_value in args.items():
        if param_value:
            groups = groups.filter(**{param_name: param_value})

    html_form = """
        <form method="get">

        <label>Group name:</label>
        <input type="text" name="first_name"><br><br>

        <label>Lessons total:</label>
        <input type="number" name="lessons_total"><br><br>

        <label>Start_date:</label>
        <input type="date" name="start_date"><br><br>

        <input type="submit" value="Submit">

       </form>
    """

    records = format_records(groups)

    response = html_form + records

    return HttpResponse(response)


@csrf_exempt
def create_group(request):

    if request.method == 'GET':

        form = GroupCreateForm()

    elif request.method == 'POST':

        form = GroupCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups')

    html_form = f"""
                <form method="post">
                {form.as_p()}
                <input type="submit" value="Submit">
                </form>
                """

    response = html_form

    return HttpResponse(response)
