from django.urls import path
from .views import index, createHouse, houses,storeHouse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",index,name="dashboard"),
    path("houses",houses,name="admin-houses"),
    path("houses/create",createHouse,name="admin-create"),
    path("houses/store",storeHouse,name="admin-store"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)