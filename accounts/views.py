from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import ProcessFormView

from .forms import AccountRegistrationForm, AccountUpdateForm, AccountUpdateProfileForm


class AccountRegistrationView(CreateView):
    model = User
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('index')
    form_class = AccountRegistrationForm


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_redirect_url(self):
        param_next = self.request.GET.get('next')
        if param_next:
            return param_next

        return reverse('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, f'User {self.request.user} has successfully logged in')
        # messages.info(self.request, f'User {self.request.user} has successfully logged in.')
        # messages.warning(self.request, f'User {self.request.user} has successfully logged in.')

        return result


class AccountLogoutView(LogoutView):
    template_name = 'accounts/logout.html'


class AccountUpdateView(ProcessFormView):
    # model = User
    # template_name = 'accounts/profile_update.html'
    # success_url = reverse_lazy('index')
    # form_class = AccountUpdateForm
    #
    # def get_object(self, queryset=None):
    #     return self.request.user

    def get(self, request, *args, **kwargs):
        user = request.user
        profile = request.user.profile

        user_form = AccountUpdateForm(instance=user)
        profile_form = AccountUpdateProfileForm(instance=profile)

        return render(
            request,
            'accounts/profile_update.html',
            {'user_form': user_form, 'profile_form': profile_form}
        )

    def post(self, request, *args, **kwargs):
        user = request.user
        profile = request.user.profile

        user_form = AccountUpdateForm(instance=user, data=request.POST)
        profile_form = AccountUpdateProfileForm(
            instance=profile,
            data=request.POST,
            files=request.FILES
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return HttpResponseRedirect(reverse('accounts:profile_update'))

        return render(
            request,
            'accounts/profile_update.html',
            {'user_form': user_form, 'profile_form': profile_form}
        )
