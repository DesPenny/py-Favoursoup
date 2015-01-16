# -*- coding: utf-8 -*-

from userena.forms import SignupFormOnlyEmail as BaseSignupForm


class SignupForm(BaseSignupForm):

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        # extend form / layout
        del self.fields['password2']
