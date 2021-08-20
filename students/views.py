from copy import copy

from core.views import EditView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from students.forms import StudentCreateForm, StudentUpdateForm, StudentsFilter
from students.models import Student


# from webargs import fields
# from webargs.djangoparser import use_args


# @use_args(
#     {
#         "first_name": fields.Str(
#             required=False
#         ),
#         "last_name": fields.Str(
#             required=False
#         ),
#         "birthdate": fields.Date(required=False),
#     },
#     location="query",
# )
# def get_students(request):
#     students = Student.objects.all().select_related('group', 'headed_group')
#
#     # for param_name, param_value in args.items():
#     #     if param_value:
#     #         students = students.filter(**{param_name: param_value})
#
#     obj_filter = StudentsFilter(data=request.GET, queryset=students)
#
#     return render(
#         request=request,
#         template_name='students/list.html',
#         context={
#             # 'students': students,
#             'obj_filter': obj_filter,
#         }
#     )
#
#
# # @csrf_exempt  # csrf token для проверки аутентификации
# # @login_required  # ограничение доступа для незарегистрированных пользователей
# def create_student(request):
#     if request.method == 'POST':
#         form = StudentCreateForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students:list'))
#
#     else:
#         form = StudentCreateForm()
#
#     return render(
#         request=request,
#         template_name='students/create.html',
#         context={
#             'form': form
#         }
#     )
#
#
# # @csrf_exempt
# def update_student(request, pk):
#     student = get_object_or_404(Student, id=pk)
#
#     if request.method == 'POST':
#         form = StudentUpdateForm(request.POST, instance=student)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students:list'))
#
#     else:
#         form = StudentUpdateForm(instance=student)
#
#     return render(
#         request=request,
#         template_name='students/update.html',
#         context={
#             'form': form
#         }
#     )
#
#
# def delete_student(request, pk):
#     student = get_object_or_404(Student, id=pk)
#
#     if request.method == 'POST':
#         student.delete()
#         return HttpResponseRedirect(reverse('students:list'))
#
#     return render(
#         request=request,
#         template_name='students/delete.html',
#         context={
#             'student': student
#         }
#     )


class UpdateStudentView(EditView):
    model = Student
    form_class = StudentUpdateForm
    success_url = 'students:list'
    template_name = 'students/update.html'


class StudentsListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'students/list.html'
    paginate_by = 10

    def get_filter(self):
        return StudentsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('group', 'headed_group')
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_filter'] = self.get_filter()

        params = self.request.GET
        if 'page' in params:
            params = copy(params)
            del params['page']
        context['get_params'] = params.urlencode()

        return context


class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Student
    template_name = 'students/create.html'
    form_class = StudentCreateForm
    success_url = reverse_lazy('students:list')


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'students/delete.html'
    success_url = reverse_lazy('students:list')
