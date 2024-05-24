from django.db import models

# Create your models here.
class Room(models.Model):
   code = models.CharField(max_length=8, default="", unique=True)   # code-unique code that identifie a room
   host = models.CharField(max_length=50, unique=True)  #one host for one room, one host cannot have multiple rooms
   # host field - store some kinda information, essentially relates to our host

   guest_can_pause = models.BooleanField(null=False, default=False)   #permission that says okay, is the guest allowed to pause the music or play the music
   votes_to_skip = models.IntegerField(null=False, default=1)
   create_at = models.DateTimeField(auto_now_add=True)  #auto_now_add- automatically add the date, time it was created at
   

