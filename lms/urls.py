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
from core.views import index

import debug_toolbar

from django.contrib import admin
from django.conf import settings # noqa
from django.urls import include, path

from students.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('hello/', hello),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('groups/', include('groups.urls')),
    path('courses/', include('courses.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
