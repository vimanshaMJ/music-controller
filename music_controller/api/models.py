from django.db import models
import string
import random

def gererate_unique_code():
    length = 6   # length of code to be

    # generate bunch of code until find one that's unique:
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))

        # make sure that code is actualyt unique:
        if Room.objects.filter(code=code).count() == 0:
            break
    return code


# Create your models here:
class Room(models.Model):
   code = models.CharField(max_length=8, default="", unique=True)   # code-unique code that identifie a room
   host = models.CharField(max_length=50, unique=True)  #one host for one room, one host cannot have multiple rooms
   # host field - store some kinda information, essentially relates to our host

   guest_can_pause = models.BooleanField(null=False, default=False)   #permission that says okay, is the guest allowed to pause the music or play the music
   votes_to_skip = models.IntegerField(null=False, default=1)
   created_at = models.DateTimeField(auto_now_add=True)  #auto_now_add- automatically add the date, time it was created at
