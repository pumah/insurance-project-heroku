from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, ReadView
#from . import views
#from .views import RiskListView

urlpatterns = {
    url(r'^risks/$', ReadView.as_view(), name="read"),
    #url(r'^risks/$', CreateView.as_view(), name="create"),
    #url(r'^risks/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    #url(r'^risk-type/$', views.risk_type, name="risk-type")
}

urlpatterns = format_suffix_patterns(urlpatterns)

