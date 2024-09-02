// This script can be used to dynamically update house details if needed

document.addEventListener('DOMContentLoaded', function() {
    const house = {
        image: 'house.jpeg',
        name: 'Luxury Villa',
        location: 'Beverly Hills, CA',
        price: '$5,000,000',
        features: [
            '5 Bedrooms',
            '4 Bathrooms',
            'Swimming Pool',
            'Garage'
        ],
        description: 'This luxurious villa is located in the heart of Beverly Hills. It features a modern design with spacious rooms, a beautiful garden, and top-notch amenities.'
    };

    document.getElementById('houseImage').src = house.image;
    document.getElementById('houseName').textContent = house.name;
    document.getElementById('houseLocation').textContent = house.location;
    document.getElementById('housePrice').textContent = house.price;
    
    const featuresList = document.getElementById('houseFeatures');
    featuresList.innerHTML = '';
    house.features.forEach(feature => {
        const li = document.createElement('li');
        li.textContent = feature;
        featuresList.appendChild(li);
    });

    document.getElementById('houseDescription').textContent = house.description;
});
