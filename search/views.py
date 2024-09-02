import json
from django.shortcuts import render
from django.db import connection
from houses.models import House
from users.models import User

# Create your views here.

def houses(request):
    sql = f"""SELECT 
            houses.*,
            users.name as ownerName,
            users.phone,
            users.email
            FROM houses 
            JOIN users 
            ON users.id=houses.ownerId_id
            WHERE houseType LIKE %s
            OR price LIKE %s 
            OR location LIKE %s """
    cursor = connection.cursor()
    cursor.execute(sql,[f"%{request.GET["type"]}%",f"%{request.GET["price"]}%",f"%{request.GET["location"]}%"])

    allHouses = cursor.fetchall()
    output = []
    for house in allHouses:
        # print(house[1])
        house_item = {
            "id":house[0],
            "name":house[1],
            "location":house[2],
            "latitude":house[3],
            "longitude":house[4],
            "price":house[5],
            "houseType":house[6],
            "description":house[7],
            "images":json.loads(house[8]) if house[8] else house[8],
            "isDeleted":house[9],
            "createdAt":house[10],
            "updatedAt":house[11],
            "ownerId":User.objects.filter(id=house[12]).first(),
            "features":json.loads(house[13]) if house[13] else house[13],
            "ownerName":house[14],
            "ownerPhone":house[15],
            "ownerEmail":house[16],
        }

        output.append(house_item)


    # print(output)

    return render(request,"search_houses.html",{"houses":output})
