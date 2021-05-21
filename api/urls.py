from django.urls import path 
from .views import FlightListView, TicketListView, AirportView

app_name = 'api'

urlpatterns = [
    path('flights/', FlightListView.as_view(), name = 'flights'),
    path('tickets/', TicketListView.as_view(), name = 'tickets'),
    path('airports/', AirportView.as_view(), name = 'airports')
]