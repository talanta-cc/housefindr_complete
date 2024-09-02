from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from users.models import User
import datetime
import time

# Create your views here.
def signUp(request):
    
    return render(request,"sign_up.html")

def store(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        password = request.POST["password"]

        password = make_password(password)

        try:
            userExists = User.objects.filter(email=email).first()
            if userExists:
                request.session["signup_error"] = f"User with email {email} already exists in our records"
                return redirect("/auth/sign-up")
            

            
            user = User()
            user.name = name
            user.email = email
            user.phone = phone

            if len(User.objects.all())<1:
                user.role = "admin"

            user.password = password
            user.createdAt = "2024-8-29 08:30"#datetime.datetime(time.time()


            user.save()
            request.session["signup_error"] = None
            return redirect("/auth/sign-in")
        except:
            request.session["signup_error"] = "Server error. Try again later"
            return redirect("/auth/sign-up")
    
    return redirect("/auth/sign-up")

def signIn(request):
    return render(request,"login.html")

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = User.objects.filter(email=email).first()
            
            if user:
                if check_password(password,user.password):
                    request.session["userId"] = user.id
                    request.session["name"] = user.name
                    request.session["email"] = user.email
                    request.session["phone"] = user.phone
                    request.session["role"] = user.role
                    request.session["error"] = None
                    return redirect("/")
                
                request.session["error"] = "Wrong password."
                return redirect("/auth/sign-in")
            
            request.session["error"] = f"No user with email {email} exists in our records"

        
            return redirect("/auth/sign-in")
        except:
            return redirect("/auth/sign-in")
    
    return redirect("/auth/sign-in")
 

def logout(request):
    request.session["userId"] = None
    request.session["name"] = None
    request.session["email"] = None
    request.session["phone"] = None
    return redirect("/")