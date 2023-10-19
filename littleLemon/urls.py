from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookingView, SingleBookingView, MenuItemView, SingleMenuItemView

urlpatterns = [
   path('api-token-auth/', obtain_auth_token),
   path('menu-items/', MenuItemView.as_view()),
   path('bookings/', BookingView.as_view()),
   path('menu-items/<str:pk>/', SingleMenuItemView.as_view()),
   path('bookings/<str:pk>/', SingleBookingView.as_view()),
]