from copy import copy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from teachers.forms import TeacherCreateForm, TeacherUpdateForm, TeachersFilter
from teachers.models import Teacher


class TeachersListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    paginate_by = 10

    def get_filter(self):
        return TeachersFilter(
            data=self.request.GET,
            queryset=self.model.objects.all()
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_filter'] = self.get_filter()

        params = self.request.GET
        if 'page' in params:
            params = copy(params)
            del params['page']
        context['get_params'] = params.urlencode()

        return context


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    template_name = 'teachers/create.html'
    form_class = TeacherCreateForm
    success_url = reverse_lazy('teachers:list')


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    template_name = 'teachers/update.html'
    form_class = TeacherUpdateForm
    success_url = reverse_lazy('teachers:list')


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    template_name = 'teachers/delete.html'
    success_url = reverse_lazy('teachers:list')
