from django.shortcuts import render
from rest_framework import generics, status
from .models import Room
from .serializers import RoomSerializer, CreateRoomSerializer
from rest_framework.views import APIView
from rest_framework.response import responses

# Create your views here.

class Roomview(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
# APIView : allow to override some default methods 
class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer

    def post(self, request, format=None):
        pass
    