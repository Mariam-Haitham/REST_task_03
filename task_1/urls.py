
from django.contrib import admin
from django.urls import path
from flights import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flights/', views.FlightsList.as_view(), name="flights-list"),
    
    path('bookings/', views.BookingsList.as_view(), name="bookings-list"), 
    path('booking/<int:booking_id>/', views.BookingDetails.as_view(), name="booking-details"),
    path('booking/<int:booking_id>/update/', views.UpdateBooking.as_view(), name="update-booking"),
    path('booking/<int:booking_id>/cancel/', views.CancelBooking.as_view(), name="cancel-booking"),
    path('book/<int:flight_id>', views.CreateBooking.as_view(), name = 'book-flight'),

    path('api/token/', TokenObtainPairView.as_view(), name='login'),
]
