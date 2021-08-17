from courses.forms import CourseCreateForm
from courses.models import Course

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView


class CoursesListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'courses/list.html'


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    template_name = 'courses/create.html'
    form_class = CourseCreateForm
    success_url = reverse_lazy('courses:list')


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    template_name = 'courses/update.html'
    form_class = CourseCreateForm
    success_url = reverse_lazy('courses:list')


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/delete.html'
    success_url = reverse_lazy('courses:list')
