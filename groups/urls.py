from django.urls import path

from groups.views import create_group, get_groups, update_group

app_name = 'groups'

urlpatterns = [
    path('', get_groups, name='list'),
    path('create/', create_group, name='create'),
    path('update/<int:id>', update_group, name='update'),
]
