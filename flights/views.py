from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import FlightListSerializer, BookingsListSerializer
from datetime import datetime

class FlightsView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer

class BookingsView(ListAPIView):
    queryset = Booking.objects.filter(date__gt=datetime.today())
    serializer_class = BookingsListSerializer
