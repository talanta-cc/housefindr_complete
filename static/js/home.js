// Slider Functionality
const sliderImages = document.querySelector('.slider-images');
const images = document.querySelectorAll('.property-card');
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');
let counter = 0;
const size = images[0].clientWidth;

nextBtn.addEventListener('click', () => {
    if (counter >= images.length - 1) return;
    sliderImages.style.transition = "transform 0.5s ease-in-out";
    counter++;
    sliderImages.style.transform = 'translateX(' + (-size * counter) + 'px)';
});

prevBtn.addEventListener('click', () => {
    if (counter <= 0) return;
    sliderImages.style.transition = "transform 0.5s ease-in-out";
    counter--;
    sliderImages.style.transform = 'translateX(' + (-size * counter) + 'px)';
});

// Heart Click Functionality
const loveEmojis = document.querySelectorAll('.love-emoji');

loveEmojis.forEach(emoji => {
    emoji.addEventListener('click', () => {
        emoji.classList.toggle('red');
    });
});


nextBtn.addEventListener('click', () => {
    if (counter >= images.length - 1) return;
    sliderImages.style.transition = "transform 0.5s ease-in-out";
    counter++;
    sliderImages.style.transform = 'translateX(' + (-size * counter) + 'px)';
});

prevBtn.addEventListener('click', () => {
    if (counter <= 0) return;
    sliderImages.style.transition = "transform 0.5s ease-in-out";
    counter--;
    sliderImages.style.transform = 'translateX(' + (-size * counter) + 'px)';
});nextBtn.addEventListener('click', () => {
    if (counter >= images.length - 1) return;
    sliderImages.style.transition = "transform 0.5s ease-in-out";
    counter++;
    sliderImages.style.transform = 'translateX(' + (-size * counter) + 'px)';
});

prevBtn.addEventListener('click', () => {
    if (counter <= 0) return;
    sliderImages.style.transition = "transform 0.5s ease-in-out";
    counter--;
    sliderImages.style.transform = 'translateX(' + (-size * counter) + 'px)';
});

// Heart Click Functionality

loveEmojis.forEach(emoji => {
    emoji.addEventListener('click', () => {
        emoji.classList.toggle('red');
    });
});

// Add Functionality to Buttons
let house_location = document.querySelector("#location");
let propertyType = document.querySelector("#property-type");
let price = document.querySelector("#max-price");

document.querySelector('.search-btn').addEventListener('click', () => {
    window.location.href = `/search?location=${house_location.value}&price=${price.value}&type=${propertyType.value}`
});

document.querySelector('.contact-btn').addEventListener('click', () => {
    //alert('Contact Us button clicked.');
});

// document.querySelectorAll('.nav-links a').forEach(link => {
//     link.addEventListener('click', () => {
//         alert(`${link.textContent} page not implemented.`);
//     });
// });
