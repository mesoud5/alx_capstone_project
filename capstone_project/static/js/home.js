document.addEventListener("DOMContentLoaded", function() {
    const backgrounds = [
        "url('../static/images/Image 1.png')",
        "url('../static/images/projects.webp')",
        "url('../static/images/skills.jpeg')"
        // Add more image paths as needed
    ];

    let currentIndex = 0;
    const body = document.body;

    function changeBackground() {
        body.style.opacity = 0;
        setTimeout(function() {
            currentIndex = (currentIndex + 1) % backgrounds.length;
            body.style.backgroundImage = backgrounds[currentIndex];
            body.style.opacity = 1;
        }, 1000); // Wait for transition to complete (1000ms = 1s)
    }

    // Change background every 7 seconds
    setInterval(changeBackground, 7000);
});
