from courses.forms import CourseCreateForm, CourseFilter
from courses.models import Course

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


# Create your views here.
def get_courses(request):
    courses = Course.objects.all()

    obj_filter = CourseFilter(data=request.GET, queryset=courses)

    return render(
        request=request,
        template_name='courses/list.html',
        context={
            'courses': courses,
            'obj_filter': obj_filter,
        }
    )


def create_course(request):
    if request.method == 'GET':

        form = CourseCreateForm()

    elif request.method == 'POST':

        form = CourseCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))

    return render(
        request=request,
        template_name='courses/create.html',
        context={
            'form': form
        }
    )


def update_course(request, pk): # noqa
    course = get_object_or_404(Course, id=pk)

    if request.method == 'POST':
        form = CourseCreateForm(request.POST, instance=course)

        if form.is_valid():
            form.save()
            print(f'Group has been saved: {course}')
            return HttpResponseRedirect(reverse('courses:list'))

    else:
        form = CourseCreateForm(instance=course)

    return render(request, 'courses/update.html', context={
            'form': form,
            'course': course
        }
    )


def delete_course(request, pk):
    course = get_object_or_404(Course, id=pk)

    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('courses:list'))

    return render(
        request=request,
        template_name='courses/delete.html',
        context={
            'course': course
        }
    )
