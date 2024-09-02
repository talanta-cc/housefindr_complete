from django.shortcuts import render,redirect
from .models import User
# Create your views here.

def index(request):
    
    if request.session.get("userId"):
        user = User.objects.filter(id=request.session.get("userId"))
        return render(request,"userprofile.html",context={"user":user})
    
    return redirect("/auth/sign-in")