from django.conf.urls import patterns, include, url
from django.contrib import admin
from testsite.home import views

urlpatterns = patterns('',
    url(r'^$', 'home.views.index')
    # Examples:
    # url(r'^$', 'my_test_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
