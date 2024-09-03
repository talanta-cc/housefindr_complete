from django.urls import path
from .views import index,view,location
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",index,name="houses"),
    path("view/<id>",view,name="view-house"),
    path("location",location,name="house-location"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

