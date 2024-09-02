from django.shortcuts import render,redirect
from django.conf import settings
from django.core.files.storage import default_storage
from houses.models import House
from users.models import User
import os
import time

# Create your views here.
def index(request):

    if not (request.session.get("role") and request.session.get("role")=="admin"):
        return redirect("/")
    return render(request,"dashboard.html")

def houses(request):
    if not (request.session.get("role") and request.session.get("role")=="admin"):
        return redirect("/")
    
    allHouses = House.objects.all()
    return render(request,"housecrud.html",{"houses":allHouses})

def createHouse(request):
    if not (request.session.get("role") and request.session.get("role")=="admin"):
        return redirect("/")
    
    owners = User.objects.all()
    return render(request,"Add_house.html",context={"owners":owners})

def addFile(file):
    #save_directory = os.path.join(settings.MEDIA_ROOT, 'houses')
    uploaded_file = file

    # Define the path where you want to save the file
    fileName = f"{time.time()}_{uploaded_file.name}"
    file_path = os.path.join(settings.MEDIA_ROOT, 'houses', fileName)

    # Save the file
    with default_storage.open(file_path, 'wb+') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)
    relative_path = os.path.join('houses', fileName)
    return relative_path

def storeHouse(request):

    if not (request.session.get("role") and request.session.get("role")=="admin"):
        return redirect("/")
    

    if request.method == "POST":
        name = request.POST["name"]
        ownerId = request.POST["ownerId"]
        location = request.POST["location"]
        houseType = request.POST["type"]
        price = request.POST["price"]
        features = request.POST["features"].split(",")
        description = request.POST["description"]

        images = []
        if request.FILES["image"] is not None:
            for file in request.FILES.getlist("image"):
                # image = open(os.path.join(f"{settings.STATIC_ROOT}/houses",file),"wb")
                image = addFile(file)
                images.append(image)

        
        try:
            house = House()
            house.name = name
            house.ownerId = User.objects.filter(id=ownerId).first()
            house.description = description
            house.location = location
            house.houseType = houseType
            house.price = price
            house.features = features
            house.images = images

            house.save()

            return redirect("/app-admin/houses")

        except:
            request.session["house_error"] = "Server error.Try again later."
            return redirect("/app-admin/houses/create")
        
    return redirect("/app-admin/houses/create")