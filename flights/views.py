from rest_framework.generics import (ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, 
		DestroyAPIView, CreateAPIView)

from datetime import datetime

from .models import Flight, Booking
from .serializers import (
	FlightSerializer, BookingSerializer, BookingDetailsSerializer, 
	UpdateBookingSerializer,  )

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer


class BookingDetails(RetrieveAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'


class UpdateBooking(RetrieveUpdateAPIView):
	queryset = Booking.objects.all()
	serializer_class = UpdateBookingSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'


class CancelBooking(DestroyAPIView):
	queryset = Booking.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'


class CreateBooking(CreateAPIView):
	serializer_class = UpdateBookingSerializer


	def perform_create(self, serializer):
		id = self.kwargs['flight_id']
		flight_obj =  Flight.objects.get(id =  id)
		serializer.save(user = self.request.user, flight = flight_obj)
