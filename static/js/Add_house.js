document.getElementById('house-form').addEventListener('submit', function(e) {
    e.preventDefault();

    // Get form data
    const name = document.getElementById('house-name').value;
    const location = document.getElementById('house-location').value;
    const type = document.getElementById('house-type').value;
    const price = document.getElementById('house-price').value;
    const description = document.getElementById('house-description').value;
    const features = document.getElementById('house-features').value;
    const image = document.getElementById('house-image').files[0];

    // Read the image file as a data URL
    const reader = new FileReader();
    reader.onload = function(e) {
        const houseData = {
            name,
            location,
            type,
            price,
            description,
            features,
            image: e.target.result // Save the image as a data URL
        };

        // Save the house data to localStorage
        let houses = JSON.parse(localStorage.getItem('houses')) || [];
        houses.push(houseData);
        localStorage.setItem('houses', JSON.stringify(houses));

        // Redirect to the view houses page
        window.location.href = 'view-houses.html';
    };
    reader.readAsDataURL(image);
});
