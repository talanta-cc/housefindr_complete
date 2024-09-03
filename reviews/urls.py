from django.urls import path
from .views import houseRating,addRating,saveRating
urlpatterns = [
    path("<house_id>",houseRating,name="house-review"),
    path("create/<house_id>",addRating,name="create-review"),
    path("save/<house_id>",saveRating,name="save-review"),
]