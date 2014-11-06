from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^accounts/', include('allauth.urls')),
    url(r'^$', 'Favoursoup.favoursoup.views.home', name='home'),
    url(r'^done/$', 'Favoursoup.favoursoup.views.done', name='done'),
    url(r'^logout/$', 'Favoursoup.favoursoup.views.logout_view', name='logout'),
    url(r'^signup/$', 'Favoursoup.favoursoup.views.signup', name='signup'),
    url(r'^signin/$', 'Favoursoup.favoursoup.views.signin', name='signin'),

    # url(r'^blog/', include('blog.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
)
