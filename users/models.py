from django.db import models

# Create your models here.
class Role(models.TextChoices):
    NORMAL_USER = "user"
    HOUSE_OWNER = "owner"
    ADMIN = "admin"


class User(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=100,choices=Role.choices, default=Role.NORMAL_USER)
    password = models.CharField(max_length=255)
    isDeleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True,)

    class Meta:
        db_table = "users"

