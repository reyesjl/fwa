document.addEventListener("DOMContentLoaded", function() {
    const carouselImages = document.querySelectorAll(".carousel img");
    let currentImageIndex = 0;

    // Function to change to the next image
    function nextImage() {
        carouselImages[currentImageIndex].style.display = 'none';
        currentImageIndex = (currentImageIndex + 1) % carouselImages.length;
        carouselImages[currentImageIndex].style.display = 'block';
    }

    // Function to change to the previous image
    function prevImage() {
        carouselImages[currentImageIndex].style.display = 'none';
        currentImageIndex = (currentImageIndex - 1 + carouselImages.length) % carouselImages.length;
        carouselImages[currentImageIndex].style.display = 'block';
    }

    // Automatic carousel change every 5 seconds
    setInterval(nextImage, 5000);

    // Optional: Link these functions to buttons
    document.getElementById('next-button').addEventListener('click', nextImage);
    document.getElementById('prev-button').addEventListener('click', prevImage);
});
