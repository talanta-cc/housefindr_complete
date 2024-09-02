// JavaScript to handle dynamic content updates

// Function to change the main image when a thumbnail is clicked
function changeMainImage(src) {
    document.getElementById('main-image').src = src;
}

// Function to toggle the "Read More" functionality in the description
document.getElementById('read-more').addEventListener('click', function() {
    const descriptionText = document.getElementById('description-text');
    descriptionText.parentElement.classList.toggle('expanded');

    if (descriptionText.parentElement.classList.contains('expanded')) {
        this.textContent = 'Read Less';
    } else {
        this.textContent = 'Read More';
    }
});

// Function to handle search button click
document.getElementById('search-button').addEventListener('click', function() {
    const query = document.getElementById('search-input').value;
    alert('Search for: ' + query); // Placeholder action for search
});
