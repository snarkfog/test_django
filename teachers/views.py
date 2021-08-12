from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from teachers.forms import TeacherCreateForm, TeacherUpdateForm, TeachersFilter
from teachers.models import Teacher


class TeachersListView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'

    def get_queryset(self):
        obj_list = TeachersFilter(
            data=self.request.GET,
            queryset=self.model.objects.all()
        )

        return obj_list


class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'teachers/create.html'
    form_class = TeacherCreateForm
    success_url = reverse_lazy('teachers:list')


class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'teachers/update.html'
    form_class = TeacherUpdateForm
    success_url = reverse_lazy('teachers:list')


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teachers/delete.html'
    success_url = reverse_lazy('teachers:list')
