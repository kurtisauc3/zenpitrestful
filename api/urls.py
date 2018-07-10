from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

'''
    routes with device/ get a full list of decives,
    routes with device/[id]/ returns just the device with that specific id
'''
urlpatterns = {
    url(r'^device/$', CreateView.as_view(), name="create"),
    url(r'^device/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
