# -*- coding: utf-8 -*-

from django.db import transaction

from userena.models import UserenaSignup
from userena import views as userena_views

from social.pipeline.partial import partial

from .forms import SignupForm


@partial
def redirect_to_signup_form(strategy, user=None, *args, **kwargs):
    if user is not None:
        return {'user': user}

    form = SignupForm(strategy.request.POST or None)
    if strategy.request.method == 'POST' and form.is_valid():
        return {
            'email': form.cleaned_data['email'],
            'password': form.cleaned_data['password1'],
        }

    return userena_views.ExtraContextTemplateView.as_view(
        template_name='userena/social_auth/signup_form.html', extra_context={
            'form': form})(strategy.request)


def create_user(strategy, details, user=None, email=None, password=None, *args, **kwargs):
    if user is not None:
        return {'user': user}

    with transaction.atomic():
        # Create new user without confirmed email
        new_user = UserenaSignup.objects.create_user(
            details['username'], None, password, False, False)

        # Send email address confirmation
        if email is not None and bool(email.strip()) is True:
            new_user.userena_signup.change_email(email)

        # Activate user automatically
        activated_user = UserenaSignup.objects.activate_user(
            new_user.userena_signup.activation_key)
        if activated_user is not False:
            new_user = activated_user

    return {'user': new_user, 'is_new': True}
