"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar

from django.contrib import admin
from django.conf import settings # noqa
from django.urls import include, path

from groups.views import create_group, get_groups, update_group

from students.views import create_student, generate_students, get_students, hello, update_student

from teachers.views import create_teacher, get_teachers, update_teacher

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('generate_students/', generate_students),
    path('students/', get_students),
    path('students/create/', create_student),
    path('students/update/<int:id>', update_student),
    path('teachers/', get_teachers),
    path('teachers/create/', create_teacher),
    path('teachers/update/<int:id>', update_teacher),
    path('groups/', get_groups),
    path('groups/create/', create_group),
    path('groups/update/<int:id>', update_group),
    path('__debug__/', include(debug_toolbar.urls)),
]
