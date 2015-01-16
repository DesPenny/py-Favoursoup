# -*- coding: utf-8 -*-

from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.functional import SimpleLazyObject
from django.core.exceptions import ObjectDoesNotExist


def get_profile(request):
    if not hasattr(request, '_cached_profile'):
        try:
            request._cached_profile = request.user.get_profile()
        except ObjectDoesNotExist:
            request._cached_profile = None
    return request._cached_profile


class ProfileMiddleware(object):

    def process_request(self, request):
        request.profile = None

        if request.user.is_authenticated():
            request.profile = SimpleLazyObject(lambda: get_profile(request))


# class EmailRequiredMiddleware(object):
#     template_name = 'profiles/messages/email_required.html'
#     key = 'EmailRequiredMiddleware'

#     def process_request(self, request, *args, **kwargs):
#         # Add message on request
#         if hasattr(request, 'session') and self.has_unconfirmed_email(request):
#             if not self.key in request.session:
#                 messages.info(request, self.get_message(request))
#                 request.session[self.key] = True  # set default value

#     def has_unconfirmed_email(self, request):
#         # skip everything for anonymous users
#         if not hasattr(request, 'user') or not request.user.is_authenticated():
#             return False

#         # skip everything for superuser / staff
#         if request.user.is_staff or request.user.is_superuser:
#             return False

#         if bool(request.user.email) is True:
#             return False

#         user = request.user
#         if hasattr(user, 'userena_signup') is True:
#             if bool(user.userena_signup.email_unconfirmed) is True:
#                 return True

#         return False

#     def get_context(self, request):
#         return {'request': request, 'user': request.user}

#     def get_message(self, request):
#         return render_to_string(self.template_name, self.get_context(request))
