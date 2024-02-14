document.addEventListener('DOMContentLoaded', function() {
    var currentImageIndex = 0;
    var images = document.querySelectorAll('.hidden-image');
    var mainImage = document.getElementById('main-image');
    
    // Load the first image into the main image element
    mainImage.src = images[currentImageIndex].src;

    function prevImage() {
        currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
        mainImage.src = images[currentImageIndex].src;
    }

    function nextImage() {
        currentImageIndex = (currentImageIndex + 1) % images.length;
        mainImage.src = images[currentImageIndex].src;
    }

    // Add event listeners to the buttons
    document.querySelector('.option-left').addEventListener('click', prevImage);
    document.querySelector('.option-right').addEventListener('click', nextImage);
});