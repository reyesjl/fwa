document.addEventListener("DOMContentLoaded", function() {
    var sliderContainer = document.querySelector('.slider-container');
    var slideWrapper = document.querySelectorAll('.slide-wrapper');
    var currentSlide = 0;
    var slideInterval = setInterval(nextSlide, 2000); // Change slide every 4 seconds

    function nextSlide() {
        slideWrapper[currentSlide].style.display = 'none';
        currentSlide = (currentSlide + 1) % slideWrapper.length;
        slideWrapper[currentSlide].style.display = 'inline-block';
    }
});