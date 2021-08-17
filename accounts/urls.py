from django.contrib.auth.views import PasswordChangeDoneView
from django.urls import path

from .views import AccountLoginView, AccountLogoutView, AccountPasswordChangeView, AccountRegistrationView, \
    AccountUpdateView

app_name = 'accounts'

urlpatterns = [
    path('registration/', AccountRegistrationView.as_view(), name='registration'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('profile_update/', AccountUpdateView.as_view(), name='profile_update'),
    path('password/', AccountPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
         name='password_change_done'),
]
