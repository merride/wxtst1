from django.conf.urls import patterns, include, url
from django.contrib import admin
from t1.views import wxinterface

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wxtst1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^weixin/jiekou/$', wxinterface.as_view(),name='jiekou'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','t1.views.index')
)
