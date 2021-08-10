from django.urls import path

from teachers.views import TeacherCreateView, TeacherDeleteView, TeacherUpdateView, TeachersListView

app_name = 'teachers'

urlpatterns = [
    # path('', get_teachers, name='list'),
    # path('create/', create_teacher, name='create'),
    # path('update/<int:id>/', update_teacher, name='update'),
    # path('delete/<int:pk>/', delete_teacher, name='delete'),
    path('', TeachersListView.as_view(), name='list'),
    path('create/', TeacherCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TeacherUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TeacherDeleteView.as_view(), name='delete'),
]
