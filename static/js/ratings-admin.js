document.addEventListener("DOMContentLoaded", function () {
    // Handle tab switching
    function openTab(evt, tabName) {
        var i, tabcontent, tablinks;

        // Hide all tab content
        tabcontent = document.getElementsByClassName("tabcontent");
        for (i = 0; i < tabcontent.length; i++) {
            tabcontent[i].style.display = "none";
        }

        // Remove active class from all tab links
        tablinks = document.getElementsByClassName("tablinks");
        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }

        // Show the current tab and add an "active" class to the button that opened the tab
        document.getElementById(tabName).style.display = "block";
        evt.currentTarget.className += " active";
    }

    // Add event listeners to tab buttons
    document.querySelectorAll('.tablinks').forEach(button => {
        button.addEventListener('click', (event) => openTab(event, button.textContent.split(' ')[0]));
    });

    // Initially show the Approved tab
    document.getElementById("Approved").style.display = "block";

    // Responsive handling: Collapse the navbar into a toggle menu for small screens
    const navbar = document.querySelector('.navbar ul');
    const toggleBtn = document.createElement('button');
    toggleBtn.classList.add('navbar-toggle');
    toggleBtn.innerHTML = '<i class="fas fa-bars"></i>';
    navbar.parentElement.insertBefore(toggleBtn, navbar);

    toggleBtn.addEventListener('click', function () {
        navbar.classList.toggle('navbar-expanded');
    });

    // Responsive adjustments on window resize
    function adjustLayout() {
        if (window.innerWidth <= 768) {
            navbar.classList.add('mobile');
            navbar.classList.remove('navbar-expanded');
        } else {
            navbar.classList.remove('mobile');
            navbar.classList.remove('navbar-expanded');
        }
    }

    // Initial layout adjustment
    adjustLayout();

    // Adjust layout on window resize
    window.addEventListener('resize', adjustLayout);
});
