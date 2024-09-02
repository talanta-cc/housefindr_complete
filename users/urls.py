from django.urls import path
from .views import index
urlpatterns = [
    path("profile",index,name="profile")
]