from django.conf.urls import patterns, include, url

from survey.views import *
from survey.forms import *

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url('^$', SurveyWizard.as_view([PageOne, PageTwo, PageThree, PageFour, PageFive]), name='rhi-form'),
    # Examples:
    # url(r'^$', 'rhi.views.home', name='home'),
    # url(r'^rhi/', include('rhi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
