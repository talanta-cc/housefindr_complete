// script.js

document.addEventListener('DOMContentLoaded', function () {
    const reviewList = document.getElementById('review-list');

    function loadReviews() {
       
        fetch('reviews.json')
            .then(response => response.json())
            .then(data => {
                displayReviews(data.reviews);
                updateRatingDistribution(data.reviews);
            });
    }

    function displayReviews(reviews) {
        reviewList.innerHTML = '';

        reviews.forEach(review => {
            const reviewItem = document.createElement('div');
            reviewItem.classList.add('review-item');
            reviewItem.innerHTML = `
                <h3>${review.username}</h3>
                <p>${'⭐'.repeat(review.rating)}</p>
                <p>${review.reviewText}</p>
                <p>${review.date}</p>
            `;
            reviewList.appendChild(reviewItem);
        });
    }

    function updateRatingDistribution(reviews) {
        const totalReviews = reviews.length;

        if (totalReviews === 0) return;

        let ratingCount = { 5: 0, 4: 0, 3: 0, 2: 0, 1: 0 };

        reviews.forEach(review => {
            ratingCount[review.rating]++;
        });

        Object.keys(ratingCount).forEach(star => {
            const percentage = (ratingCount[star] / totalReviews) * 100;
            document.querySelector(`.rating-bar:nth-child(${6 - star}) .filled-bar`).style.width = `${percentage}%`;
        });

        const overallRating = Object.keys(ratingCount).reduce((total, star) => total + (star * ratingCount[star]), 0) / totalReviews;
        document.querySelector('.overall-rating h3').textContent = `${overallRating.toFixed(1)}/5`;
        document.querySelector('.overall-rating p').textContent = `${totalReviews} verified ratings`;
    }

    loadReviews();
});
