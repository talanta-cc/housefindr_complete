import json
from django.shortcuts import render,redirect
from django.db import connection
from houses.models import House
from django.conf import settings

from users.models import User
from reviews.models import Review

# Create your views here.
def index(request):
    houses = House.objects.all()
    print(settings.MEDIA_URL)
    
    return render(request,"houses.html",{"houses":houses})

def view(request,id):
    house = House.objects.filter(id=id).first()
    sql = f"""SELECT 
            houses.*,
            users.name as ownerName,
            users.phone,
            users.email
            FROM houses 
            JOIN users 
            ON users.id=houses.ownerId_id
            """
    cursor = connection.cursor()
    cursor.execute(sql,[])

    allHouses = cursor.fetchone()
    output = []

    house_item = {
            "id":allHouses[0],
            "name":allHouses[1],
            "location":allHouses[2],
            "latitude":allHouses[3],
            "longitude":allHouses[4],
            "price":allHouses[5],
            "houseType":allHouses[6],
            "description":allHouses[7],
            "images":json.loads(allHouses[8]) if allHouses[8] else allHouses[8],
            "isDeleted":allHouses[9],
            "createdAt":allHouses[10],
            "updatedAt":allHouses[11],
            "ownerId":User.objects.filter(id=allHouses[12]).first(),
            "features":json.loads(allHouses[13]) if allHouses[13] else allHouses[13],
            "ownerName":allHouses[14],
            "phone":allHouses[15],
            "ownerEmail":allHouses[16],
    }

    reviews = Review.objects.filter(houseId=house).all()
    return render(request,"description.html",{"house":house_item,"reviews":reviews})

def create(request):
    return render(request,"create.html")

def store(request):
    name = request.POST["name"]
    House.objects.create(name="House 1")
    return redirect("/admin/houses")

def edit(request,id):
    house = House.objects.filter(id=id).first()

    return render(request,"edit.html",{"house":house})

def update(request,id):
    house = House.objects.filter(id=id).first()
    return redirect("/houses")

def location(request):
    return render(request,"location.html")

def delete(request,id):
    house = House.objects.update(isDeleted=True)
    return redirect("/houses")