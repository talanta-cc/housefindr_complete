from django.urls import path
from .views import home,aboutus,contactus
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",home,name="home"),
    path("aboutus",aboutus,name="aboutus"),
    path("contactus",contactus,name="contactus"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

