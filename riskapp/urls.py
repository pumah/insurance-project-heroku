from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateRiskView, DetailsView, ReadView, TypeCreate, RfldCreate
from . import views

urlpatterns = {
    url(r'^risks/$', ReadView.as_view(), name="read"),
    url(r'^risks/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    url(r'^RiskTypeCreate/$',views.TypeCreate.as_view(), name='risktypecreate'),
    url(r'^RiskFieldCreate/$',views.RfldCreate.as_view(), name='riskfieldcreate'),
}

urlpatterns = format_suffix_patterns(urlpatterns)

