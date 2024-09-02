from django.shortcuts import render
from houses.models import House

# Create your views here.
def home(request):
    houses = House.objects.all()
    print(request.session.get("userId"))
    return render(request,"home.html",context={"houses":houses})


def aboutus(request):
    houses = House.objects.all()
    return render(request,"About_us.html")


def contactus(request):
    houses = House.objects.all()
    return render(request,"contactus.html")