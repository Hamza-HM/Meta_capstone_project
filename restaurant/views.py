from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .models import *
from .serializers import *

# Create your views here.
class BookingViewSet(viewsets.ModelViewSet):    
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (IsAuthenticated,)

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer
    
        
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request, *args, **kwargs):
    return Response({"message":"This view is protected"})

def hello_static(request, *args, **kwargs):
    return render(request, 'index.html', {})