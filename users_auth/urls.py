from django.urls import path
from .views import signIn, signUp,store,login,logout
urlpatterns = [
    path("sign-up",signUp,name="sign-up"),
    path("sign-in",signIn,name="sign-in"),
    path("store",store,name="store"),
    path("login",login,name="login"),
    path("logout",logout,name="logout"),
]