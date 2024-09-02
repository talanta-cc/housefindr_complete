from django.db import models
from houses.models import House
from users.models import User

# Create your models here.

class Booking(models.Model):
    houseId = models.ForeignKey(House,on_delete=models.CASCADE)
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
    isDeleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=False)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "bookings"