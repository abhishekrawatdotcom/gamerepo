from django.db import models
from django.core.cache import cache
import datetime
from androidgameproject import settings

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    Game_id = models.IntegerField()
    Username=models.CharField(max_length=50,)
    Create_time=models.DateTimeField(auto_now_add=True)
    Game=models.CharField(max_length=50,default="")
    Level=models.IntegerField(default=0)
    Pay_per_round=models.IntegerField(default=0)
    Uuid=models.IntegerField()



class Games(models.Model):
    Game_id=models.AutoField(primary_key=True)
    Game_name=models.CharField(max_length=50)

class File(models.Model):
    image = models.ImageField(upload_to='game/image', default="")



class allview(models.Model):
    gameimg=models.ImageField(upload_to='allview/image', default="")
    title=models.CharField(max_length=50,default='')
    desc=models.CharField(max_length=100,default='')
