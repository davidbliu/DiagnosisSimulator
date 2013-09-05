from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^illness_form/(?P<illnessID>\d+)/$', 'Illness.views.illness_form'),
    url(r'^list/$', 'Illness.views.illness_list_view'),
    url(r'^clues/$', 'Illness.views.symptoms_clues_view'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
