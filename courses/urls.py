from courses.views import CourseCreateView, CourseDeleteView, CourseUpdateView, CoursesListView

from django.urls import path

app_name = 'courses'

urlpatterns = [
    path('', CoursesListView.as_view(), name='list'),
    path('create/', CourseCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CourseUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CourseDeleteView.as_view(), name='delete'),
]
