from django.urls import path

from teachers.views import create_teacher, get_teachers, update_teacher

app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list'),
    path('create/', create_teacher, name='create'),
    path('update/<int:id>', update_teacher, name='update'),
]
