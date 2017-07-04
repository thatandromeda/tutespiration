from django.conf.urls import include, url
from django.contrib import admin

from tutespiration.core.views import Tutespiration, CitableTutespiration, custom404

urlpatterns = [
    # Examples:
    # url(r'^$', 'tutespiration.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Tutespiration.as_view()),
    url(r'^(?P<pk>\d+)/$',
        CitableTutespiration.as_view(), name='citable'),
    url(r'^random/$',
        CitableTutespiration.as_view(), name='random'),
]

handler404 = custom404
