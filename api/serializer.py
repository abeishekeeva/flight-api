from rest_framework import serializers
from flights.models import Flights

class FlightSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Flights 
        fields = ['flight_no', 'scheduled_departure', 'scheduled_arrival', 'departure_airport',
                  'arrival_airport', 'status']
