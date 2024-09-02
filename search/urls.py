from django.urls import path
from .views import houses
urlpatterns = [
    path("",houses,name="search-houses")
]