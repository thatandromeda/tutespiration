from django.conf.urls import include, url
from django.contrib import admin

from tutespiration.core.views import Tutespiration, CitableTutespiration

urlpatterns = [
    # Examples:
    # url(r'^$', 'tutespiration.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Tutespiration.as_view()),
    url(r'^(?P<font>\d+)/(?P<pk>\d+)/(?P<photo>[\d\w\-_]+)/$',
        CitableTutespiration.as_view()),
]
