from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    url(r'^detail/(?P<illnessID>\d+)/$', 'Illness.views.illness_detail_view'),
    url(r'^list/$', 'Illness.views.illness_list_view'),
    url(r'^home/$', 'Illness.views.home_view'),

    #url configs for simulator views
    url(r'^getClues/$', 'Illness.simulator.get_clues_view'),
    url(r'^getSymptoms/$', 'Illness.simulator.get_symptoms_view'),
    url(r'^simulator/(?P<illnessID>\d+)/$', 'Illness.simulator.simulator_view'),

    #below are urls for forms
    url(r'^add_illness_form/$', 'Illness.forms.add_illness_form'),
    url(r'^filterSymptoms/$', 'Illness.forms.filter_symptom_view'),
    url(r'^illness_form/(?P<illnessID>\d+)/$', 'Illness.forms.illness_form'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
