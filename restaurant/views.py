from django.shortcuts import render
<<<<<<< HEAD

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import *
from .serializers import *

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
=======
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User
from restaurant.models import Booking, Menu
from restaurant.serializers import BookingSerializer, MenuSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def index(request):
    return render(request, "index.html", {})

>>>>>>> 158c1d284bef6649668e2917c87e124698bc6d72

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
<<<<<<< HEAD
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated] 

# @api_view()
# @permission_classes([IsAuthenticated])
# # @authentication_classes([TokenAuthentication])
# def msg(request):
#     return Response({"message":"This view is protected"})
    
=======


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class UsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
>>>>>>> 158c1d284bef6649668e2917c87e124698bc6d72
