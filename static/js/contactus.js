document.getElementById("contactForm").addEventListener("submit", function(event) {
    event.preventDefault();

    // Get form values
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;

    // Display a success message
    const formMessage = document.getElementById("formMessage");
    formMessage.textContent = `Thank you, ${name}! Your message has been sent.`;
    formMessage.style.color = "green";

    // Clear form fields
    document.getElementById("contactForm").reset();
});
