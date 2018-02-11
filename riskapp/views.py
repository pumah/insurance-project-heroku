from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import riskSerializer
from .models import risk_type, risk_field
from django.views.generic.edit import CreateView
'''
from rest_framework.response import Response

class RiskListView(generics.ListCreateAPIView):

    def get(self, request, format = None):
        risks = risk_type.objects.all()
        serializer = riskfldSerializer(risks, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = riskfldSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
'''
class CreateRiskView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = risk_type.objects.all()
    serializer_class = riskSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new risk."""
        serializer.save()

#class DetailsView(generics.RetrieveUpdateDestroyAPIView):
 #   """This class handles the http GET, PUT and DELETE requests."""

 #   queryset = risk_type.objects.all()
 #   serializer_class = riskSerializer

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




