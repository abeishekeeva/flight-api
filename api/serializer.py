from rest_framework import serializers
from flights.models import Flights, AirportsData
from tickets.models import Tickets 

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights 
        fields = ['flight_no', 'scheduled_departure', 'scheduled_arrival', 'departure_airport', 'arrival_airport', 'status']

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets 
        fields = ['ticket_no', 'passenger_id', 'passenger_name']
    
class AirportDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportsData
        fields = ['airport_code', 'airport_name', 'city', 'coordinates', 'timezone']

        
