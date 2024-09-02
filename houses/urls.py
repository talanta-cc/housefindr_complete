from django.urls import path
from .views import index,view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",index,name="houses"),
    path("view/<id>",view,name="view-house"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

