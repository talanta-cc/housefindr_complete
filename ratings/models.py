from django.db import models
from users.models import User
from houses.models import House
# Create your models here.
class Rating(models.Model):
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
    houseId = models.ForeignKey(House,on_delete=models.CASCADE)
    stars = models.IntegerField()
    review = models.CharField(max_length=1000,null=True)
    isAccepted = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=False)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "ratings"