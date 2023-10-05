from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
# Create your views here.

from .models import *
from .serializers import *

class BookingViewSet(viewsets.ModelViewSet):    
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (IsAuthenticated,)

class MenuItemsView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
        
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer