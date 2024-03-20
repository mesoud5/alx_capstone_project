document.addEventListener('DOMContentLoaded', function () {
    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const upperNav = document.getElementById("upper-nav");

    hamburgerMenu.addEventListener('click', function () {
        upperNav.classList.toggle('show');
    });
});
