import re

from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from profiles.forms import SignupForm

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/signup/$', 'userena.views.signup', {
        'signup_form': SignupForm,
        }, name='userena_signup'),
    url(r'^accounts/', include('userena.urls')),
)

urlpatterns += patterns('Favoursoup.favoursoup.views',
    url(r'^$', 'home', name='home'),
    url(r'^done/$', 'done', name='done'),
)

urlpatterns += patterns('',
    url('', include('social.apps.django_app.urls', namespace='social')),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), 'serve'),
    )

    urlpatterns += patterns('django.views.static',
        url(r'^%s(?P<path>.*)$' % re.escape(settings.MEDIA_URL.lstrip('/')), 'serve', kwargs={
            'document_root': settings.MEDIA_ROOT,
        }),
    )
