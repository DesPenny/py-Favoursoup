"""
Django settings for Favoursoup project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rh39!wl9tk1-q7t)dl+&s-!!wu=oe^+6v!mu7r$o2d1$i!_%5n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'Favoursoup.favoursoup',
    'social.apps.django_app.default',
    'allauth',
    'allauth.account',


)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.twitter.TwitterOAuth',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.linkedin.LinkedinOAuth2',
    'social.backends.google.GoogleOAuth2',
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",

)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)


#Facebook Auth
SOCIAL_AUTH_FACEBOOK_KEY = '1501771236726203'
SOCIAL_AUTH_FACEBOOK_SECRET = '8f94a1a58a7fe16df796094504bc7e80'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'ru_RU'}

#Google+ Auth
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '998998365128-l5vh4lprl621mj7gcf14k42bmmk1qa5o.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '3lzJgKnT_f5Htb7WIQB2esxz'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email', 'profile']

#Linkedin Auth
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '75dl1hlzpa027k'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'jFkcEcCP5z88eT4d'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_basicprofile', 'r_emailaddress', 'w_messages']
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = [('id', 'id'),
                                   ('firstName', 'first_name'),
                                   ('lastName', 'last_name'),
                                   ('emailAddress', 'email_address'),
                                   ('headline', 'headline'),
                                   ('industry', 'industry')]

#Twitter Auth
SOCIAL_AUTH_TWITTER_KEY = 'tv71Nt7TJLnNSK3GHO4am2nlc'
SOCIAL_AUTH_TWITTER_SECRET = 'BeLh97LXecsOKSCUTRyjFMmCVH5gNgsOIE5NKyJ4qq0u6dOkGf'


SOCIAL_AUTH_PIPELINE = (
    # Get the information we can about the user and return it in a simple
    # format to create the user instance later. On some cases the details are
    # already part of the auth response from the provider, but sometimes this
    # could hit a provider API.
    'social.pipeline.social_auth.social_details',

    # Get the social uid from whichever service we're authing thru. The uid is
    # the unique identifier of the given user in the provider.
    'social.pipeline.social_auth.social_uid',

    # Verifies that the current auth process is valid within the current
    # project, this is were emails and domains whitelists are applied (if
    # defined).
    'social.pipeline.social_auth.auth_allowed',

    # Checks if the current social-account is already associated in the site.
    'social.pipeline.social_auth.social_user',

    # Make up a username for this person, appends a random string at the end if
    # there's any collision.
    'social.pipeline.user.get_username',

    # Send a validation email to the user to verify its email address.
    # Disabled by default.
    # 'social.pipeline.mail.mail_validation',

    # Associates the current social details with another user account with
    # a similar email address. Disabled by default.
     'social.pipeline.social_auth.associate_by_email',

    # Create a user account if we haven't found one yet.
    'social.pipeline.user.create_user',

    # Create the record that associated the social account with this user.
    'social.pipeline.social_auth.associate_user',

    # Populate the extra_data field in the social record with the values
    # specified by settings (and the default ones like access_token, etc).
    'social.pipeline.social_auth.load_extra_data',

    # Update the user record with any changed info from the auth service.
    'social.pipeline.user.user_details'
)

SOCIAL_AUTH_DISCONNECT_PIPELINE = (
    # Verifies that the social association can be disconnected from the current
    # user (ensure that the user login mechanism is not compromised by this
    # disconnection).
    'social.pipeline.disconnect.allowed_to_disconnect',

    # Collects the social associations to disconnect.
    'social.pipeline.disconnect.get_entries',

    # Revoke any access_token when possible.
    'social.pipeline.disconnect.revoke_tokens',

    # Removes the social associations.
    'social.pipeline.disconnect.disconnect'
)



ROOT_URLCONF = 'Favoursoup.urls'

WSGI_APPLICATION = 'Favoursoup.wsgi.application'

SITE_ID = 1

LOGIN_URL = "/"

LOGIN_REDIRECT_URL = "/"

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = False
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = LOGIN_REDIRECT_URL
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 10
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = None
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Subject is: "
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_URL
ACCOUNT_SIGNUP_FORM_CLASS = None
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION =True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD ="email"
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"

ACCOUNT_USERNAME_MIN_LENGTH =4
ACCOUNT_USERNAME_REQUIRED =False
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE =False
ACCOUNT_PASSWORD_MIN_LENGTH =6
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION =True

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/favoursoup/Favoursoup/db.sqlite',
               'USER': '',
               'PASSWORD': '',
               'HOST': '',
               'PORT': ''
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/



STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "static", "static-only")

#STATICFILES_DIRS = (
 #   os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "static", "static"),


TEMPLATE_DIRS = (
        '/home/favoursoup/Favoursoup/Favoursoup/favoursoup/static/templates',
)

#MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "static", "media")

STATIC_URL = '/static/'