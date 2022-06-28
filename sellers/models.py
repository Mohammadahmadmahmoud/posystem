from django.db import models
import uuid

# Create your models here.

class Shop(models.Model):
   user_id = models.IntegerField()
   shop_id = models.UUIDField(default=uuid.uuid4, unique=True)
   name = models.CharField(max_length=255)   
   description = models.CharField(max_length=255)
   logo = models.CharField(max_length=255)

class Item(models.Model):
   shop_id = models.UUIDField(default=uuid.uuid4, unique=True)
   name = models.CharField(max_length=255)
   description = models.CharField(max_length=255)
   price = models.FloatField()
   shop_id = models.UUIDField()

class ItemPicture(models.Model):
   shop_id = models.UUIDField(default=uuid.uuid4, unique=True)
   img_url = models.CharField(max_length=255)
   