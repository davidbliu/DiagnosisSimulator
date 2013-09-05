from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^add_illness_form/$', 'Illness.views.add_illness_form'),
    url(r'^illness_form/(?P<illnessID>\d+)/$', 'Illness.views.illness_form'),
    url(r'^list/$', 'Illness.views.illness_list_view'),

    #url configs for simulator views
    url(r'^getClues/$', 'Illness.simulator.get_clues_view'),
    url(r'^simulator/(?P<illnessID>\d+)/$', 'Illness.simulator.simulator_view'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
