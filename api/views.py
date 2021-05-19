from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.serializers import Serializer
from flights.models import Flights 
from .serializer import FlightSerializer

class FlightListView(ListAPIView):
    queryset = Flights.objects.all()[:10]
    serializer_class = FlightSerializer
