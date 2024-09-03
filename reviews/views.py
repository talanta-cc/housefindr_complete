from django.shortcuts import render,redirect
from houses.models import House
from .models import Review
from users.models import User
from django.db import connection

# Create your views here.
def houseRating(request,house_id):
    house = House.objects.filter(id=house_id).first()
    reviews = Review.objects.filter(houseId=house).all()
    reviews = []

    sql = f"""SELECT 
            reviews.id,
            reviews.stars,
            reviews.comment,
            reviews.createdAt,
            users.name
            FROM reviews 
            JOIN users 
            ON users.id=reviews.userId_id
            """
    cursor = connection.cursor()
    cursor.execute(sql,[])
    results = cursor.fetchall()
    for result in results:
        item = {
            "id":result[0],
            "stars":result[1],
            "comment":result[2],
            "createdAt":result[3],
            "name":result[4],
        }
        reviews.append(item)
    return render(request,"review.html",{"reviews":reviews,"house":house})

def addRating(request,house_id):
    if not request.session.get("userId"):
        return redirect("/auth/sign-in")
    
    house = House.objects.filter(id=house_id).first()
    return render(request,"ratings.html",{"house":house})

def saveRating(request,house_id):
    if request.method == "POST":
        
        user = User.objects.filter(id=request.session.get("userId")).first()
        house = House.objects.filter(id=house_id).first()
        stars = request.POST.get("stars")
        comment = request.POST["comment"]
        
        if not stars:
            return redirect(f"/reviews/create/{house_id}")
        review = Review()
        review.userId = user
        review.houseId = house
        review.stars = stars
        review.comment = comment

        review.save()

        return redirect(f"/reviews/{house_id}")