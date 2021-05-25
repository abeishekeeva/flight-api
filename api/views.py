from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from rest_framework.response import Response 
from flights.models import Flights, AirportsData
from .serializer import FlightSerializer, AirportDataSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

class FlightListView(ListAPIView):
    queryset = Flights.objects.all()[:10]
    serializer_class = FlightSerializer


class AirportView(APIView):    
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        airport_code = request.query_params.get('code', None)
        if 'code' in request.query_params and not len(airport_code):
            return Response({'error_msg': "Please enter airport code"})
        if 'code' not in request.query_params:
            queryset = AirportsData.objects.all()       
            res = AirportDataSerializer(queryset, many=True)         
            return Response(res.data)
        else:
            queryset = AirportsData.objects.filter(airport_code=airport_code)             
            if not queryset: 
                return Response({"error_msg": "No airport is found"}) 
            else:
                res = AirportDataSerializer(queryset, many=True)
                return Response(res.data)

        
    def post(self, request):
        new_data = request.data 
        serializer = AirportDataSerializer(data=new_data)
        if serializer.is_valid(): 
            serializer.save()
            return Response({"success": True, "message": "New airport data created"})
        else:
            return Response({"success": False, "message": "Please provide valid information"})

    def delete():
        #delete aiport by code 
        pass 

    def update():
        #update airport info by code 
        pass 

    #В serializers: вытащить полеты аэропорта в get api (Nested Serializer) 
    #Почитать про authentication 


    
