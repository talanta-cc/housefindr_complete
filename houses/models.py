from django.db import models
from users.models import User

# Create your models here.
class HouseType(models.TextChoices):
    SINGLEROOM = "single room"
    BEDSITTER = "bedsitter"
    ONEBEDROOM = "one bedroom"
    TWOBEDROOM = "two bedroom"
    THREEBEDROOM = "three bedroom"
    FOURBEDROOM = "four bedroom"
    OWNCOMPOUND = "own compound"

class House(models.Model):
    ownerId = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    latitude = models.CharField(max_length=100,null=True)
    longitude = models.CharField(max_length=100,null=True)
    price = models.CharField(max_length=100,null=True)
    houseType = models.CharField(max_length=100,choices=HouseType.choices,default=HouseType.SINGLEROOM)
    description = models.CharField(max_length=1000,null=True)
    features = models.JSONField(max_length=1000,null=True)
    images = models.JSONField(max_length=1000,null=True)
    isDeleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "houses"

