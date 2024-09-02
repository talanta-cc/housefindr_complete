document.addEventListener("DOMContentLoaded", function() {
    const profileCard = document.querySelector('.profile-card');
    const leftSide = document.querySelector('.left-side');
    const rightSide = document.querySelector('.right-side');

    function adjustLayout() {
        if (window.innerWidth <= 768) { // Tablet and smaller devices
            profileCard.style.flexDirection = 'column';
            leftSide.style.width = '100%';
            leftSide.style.borderRight = 'none';
            rightSide.style.width = '100%';
            rightSide.style.marginTop = '20px';
            rightSide.style.padding = '10px';
        } else { // Larger devices
            profileCard.style.flexDirection = 'row';
            leftSide.style.width = '35%';
            leftSide.style.borderRight = '1px solid #ddd';
            rightSide.style.width = '65%';
            rightSide.style.marginTop = '0';
            rightSide.style.padding = '20px';
        }
    }

    // Run on initial load
    adjustLayout();

    // Run on window resize
    window.addEventListener('resize', adjustLayout);
});
