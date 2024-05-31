from rest_framework import serializers
from .models import Room

# Serialization is the process of converting complex data into a format that can be easily transmitted and stored.

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')     # mathes to objects in Room class in models.py
        
# going to send a POST request to the end point we set up here        
class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')