from django.urls import path 
from .views import FlightListView

app_name = 'api'

urlpatterns = [
    path('flights/', FlightListView.as_view(), name='flights')
]