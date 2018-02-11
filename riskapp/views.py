from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import riskSerializer
from .models import risk_type, risk_field
from django.views.generic.edit import CreateView

class CreateRiskView(generics.ListCreateAPIView):
    queryset = risk_type.objects.all()
    serializer_class = riskSerializer

    def perform_create(self, serializer):
        serializer.save()

class ReadView(generics.ListAPIView):
    queryset = risk_type.objects.all()
    serializer_class = riskSerializer

class DetailsView(generics.RetrieveAPIView):
    queryset = risk_type.objects.all()
    serializer_class = riskSerializer

class TypeCreate(CreateView):
    model = risk_type
    fields = ['risk_type']

    def dispatch(self, *args, **kwargs):
            return super(TypeCreate, self).dispatch(*args, **kwargs)

class RfldCreate(CreateView):
    model = risk_field
    fields = ['risk_type','field_name','field_type','field_metadata']

    def dispatch(self, *args, **kwargs):
            return super(RfldCreate, self).dispatch(*args, **kwargs)
