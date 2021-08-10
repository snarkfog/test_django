from django.urls import path

from students.views import StudentUpdateView, create_student, delete_student, generate_students, get_students

app_name = 'students'

urlpatterns = [
    path('generate_students/', generate_students),
    path('', get_students, name='list'),
    path('create/', create_student, name='create'),
    # path('update/<int:id>/', update_student, name='update'),
    # path('update/<int:pk>/', UpdateStudentView.update_object, name='update'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', delete_student, name='delete'),
]
