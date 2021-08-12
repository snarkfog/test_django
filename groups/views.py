from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from groups.forms import GroupCreateForm, GroupUpdateForm
from groups.models import Group

from students.models import Student


class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'


class GroupCreateView(CreateView):
    model = Group
    template_name = 'groups/create.html'
    form_class = GroupCreateForm
    success_url = reverse_lazy('groups:list')


class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'groups/update.html'
    form_class = GroupUpdateForm
    success_url = reverse_lazy('groups:list')

    pk_url_kwarg = 'ppk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_object().students.select_related('group', 'headed_group').all()

        return context

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.id
        except AttributeError as ex:  # noqa
            pass

        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        form.instance.headman = Student.objects.get(id=form.cleaned_data['headman_field'])
        form.instance.save()

        return response


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'groups/delete.html'
    success_url = reverse_lazy('groups:list')
