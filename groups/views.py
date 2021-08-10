from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from groups.forms import GroupCreateForm, GroupsFilter
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

    # for param_name, param_value in args.items():
    #     if param_value:
    #         groups = groups.filter(**{param_name: param_value})

    obj_filter = GroupsFilter(data=request.GET, queryset=groups)

    return render(
        request=request,
        template_name='groups/list.html',
        context={
            'groups': groups,
            'obj_filter': obj_filter,
        }
    )


# @csrf_exempt
def create_group(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    elif request.method == 'POST':
        form = GroupCreateForm(data=request.POST)
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

    if request.method == 'POST':
        form = GroupCreateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            print(f'Group has been saved: {group}')
            return HttpResponseRedirect(reverse('groups:list'))
    else:
        form = GroupCreateForm(instance=group)

    return render(request, 'groups/update.html', context={
        'form': form,
        # 'group': group,
        'students': group.students.select_related('group', 'headed_group').all()
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


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupCreateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_object().students.select_related('group', 'headed_group').all()

        return context
