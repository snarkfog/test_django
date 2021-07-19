from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from groups.forms import GroupCreateForm, GroupUpdateForm
from groups.models import Group

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

    return render(
        request=request,
        template_name='groups/list.html',
        context={
            'groups': groups
        }
    )


# @csrf_exempt
def create_group(request):

    if request.method == 'GET':

        form = GroupCreateForm()

    elif request.method == 'POST':

        form = GroupCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/create.html',
        context={
            'form': form
        }
    )


# Homework 10
# @csrf_exempt
def update_group(request, id): # noqa

    group = get_object_or_404(Group, id=id)

    if request.method == 'GET':

        form = GroupUpdateForm(instance=group)

    elif request.method == 'POST':

        form = GroupUpdateForm(
            instance=group,
            data=request.POST
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/update.html',
        context={
            'form': form
        }
    )


# Homework 12
def delete_group(request, pk):
    group = get_object_or_404(Group, id=pk)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/delete.html',
        context={
            'group': group
        }
    )
