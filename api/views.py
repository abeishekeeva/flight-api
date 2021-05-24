from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from flights.models import Flights, AirportsData
from tickets.models import Tickets 
from .serializer import FlightSerializer, TicketSerializer, AirportDataSerializer 
from rest_framework.response import Response

class FlightListView(ListAPIView):
    queryset = Flights.objects.all()[:10]
    serializer_class = FlightSerializer 

class TicketListView(ListAPIView):
    queryset = Tickets.objects.all()[:7]
    serializer_class = TicketSerializer 

# class FlightView(generics.RetrieveAPIView):
#     lookup_field = 'flight_no'
#     queryset = Flight.objects.all()

class AirportView(APIView):

    def get(self, request):
        airport_code = request.query_params.get('code')
        if 'code' in request.query_params and len(airport_code) == 0:
            return Response({'error_msg': 'Please input airport code'})
        if 'code' not in request.query_params:
            queryset = AirportsData.objects.all() 
            res = AirportDataSerializer(queryset, many = True) 
            return Response(res.data)
        else:
            queryset = AirportsData.objects.filter(airport_code = airport_code)
            # print(queryset is None)
            if not queryset:
                return Response({'error_msg': 'No airport found'})
            else:
                res = AirportDataSerializer(queryset, many=True)
                return Response(res.data)


    def post(self, request):
        new_data = request.data 
        serializer = AirportDataSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'message': 'New airport data created'})
        else:
            return Response({'success': False, 'message': 'Please provide valid information'})


    # def delete(self, request):
    #     airport_code = request.query_params.get('code')
    #     snippet = self.get_object(airport_code)
    #     snippet.delete()
    #     return Response({'success':True, 'message': 'Airport deleted from DB'})
    #     #delete airport by code
        


    # def delete(self, request, pk):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
    # def delete(self, request, pk):
    # snippet = self.get_object(pk)
    # snippet.delete()
    # return Response(status=status.HTTP_204_NO_CONTENT)

    def update():
        #update airport by code
        pass 
    
    #В serializers по аэропорту вытащить все полеты аэропорта 
    #Прочитать про authentication 